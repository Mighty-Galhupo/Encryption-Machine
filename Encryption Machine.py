ALPHABET = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
SPECIAL_CHARACTERS = (" ", "!", "?", ".", ",", ":", "(", ")", "'")
VALID_KEY_PARTS = ("A", "B", "C", "D")
DEFAULT_KEY = "ADCBDACBDCABCDBCBDDACB"
DEFAULT_SEED = 423543247642687464872689217

def message_encrypter():	# Setup and user input
	operation = None
	encryption_key_validity = False
	message_validity = False
	
	print("Do you want to encrypt or decrypt a message?")
	while operation != 1 and operation != -1:	# To be multiplied later so as to add or subtract letter positions 
		user_operation = input().lower()
		if user_operation == "encrypt":
			operation = 1
		elif user_operation == "decrypt":
			operation = -1
		else:
			print("Please input a valid operation: encrypt or decrypt.")
	
	print("Operation accepted!")
			
	print("Please enter the encryption key. (Combination of {} or nothing for default)".format(VALID_KEY_PARTS))
	while encryption_key_validity == False:	# Check encryption key composition
		encryption_key = input().upper()
		encryption_key_validity = True
		if encryption_key == "":
			encryption_key = DEFAULT_KEY
		else:
			for x in encryption_key:
				if x not in VALID_KEY_PARTS:
					encryption_key_validity = False
			if encryption_key_validity == False:
				print("Please input a valid encryption key. (Combination of {} or nothing for default)".format(VALID_KEY_PARTS))

	print("Key accepted!")

	print("Please input the message.")
	while message_validity == False:
		message_validity = True
		message = input()
		for x in message:
			if x.lower() not in ALPHABET and x not in SPECIAL_CHARACTERS:
				message_validity = False
		if message_validity == False:
			print("Please input a valid message.")

	print("Message accepted!")
			
	print("Your {} message is '{}'".format(user_operation + "ed", message_shifter(operation, encryption_key, message)))


def message_shifter(operation, encryption_key, message):	# Actually encrypts or decrypts messages
	for x in encryption_key[::operation]:
		letter_counter = 1
		new_message = ""
		if x == "D":
			substitution_guide = letter_substitution_randomizer()
		for y in message:
			if y in SPECIAL_CHARACTERS:
				new_message = new_message + y
			else:
				is_upper = y == y.upper()
				y = y.lower()
				old_letter_index = ALPHABET.index(y)
				if x == "A":	# Shift each letter by the position the letter occupies in the message
					new_letter_index = old_letter_index + letter_counter * operation
				elif x == "B":	# Shift each letter by the ammount of letters until the end of the message
					new_letter_index = old_letter_index + (len(message) - (letter_counter - 1)) * operation
				elif x == "C":	# Shift each letter by 2 (Caesar Cypher)
					new_letter_index = old_letter_index + 2 * operation
				elif x == "D":	# Generates a substitution table then swaps letters accordingly
					if operation == 1:
						new_letter_index = ALPHABET.index(substitution_guide[y])
					elif operation == -1:
						for z in substitution_guide:
							if substitution_guide[z] == y:
								new_letter_index = ALPHABET.index(z)

				while len(ALPHABET) - 1 < new_letter_index:	# Ensures the new letter is a valid one
					new_letter_index = new_letter_index - len(ALPHABET)
				while new_letter_index < 0:
					new_letter_index = new_letter_index + len(ALPHABET)
				if is_upper:
					new_message = new_message + ALPHABET[new_letter_index].upper()
				else:
					new_message = new_message + ALPHABET[new_letter_index]

			letter_counter = letter_counter + 1
		message = new_message

	return message 
	
def letter_substitution_randomizer():
	letters = list(ALPHABET)
	shuffled = letters.copy()
	letter_maps_to_itself = True
	seed = None

	while seed == None:
		print("Choose a seed (positive integer) for the substitution cipher to use (or nothing for default).")
		try:
			seed = int(input())
		except:
			pass

		if seed == None:
			seed = DEFAULT_SEED

		elif seed <= 0:
			seed = None

		if seed == None:
			print("Please choose a valid seed (positive integer or nothing for default).")
		
	print("Seed accepted!")

	while letter_maps_to_itself:
		seed = letter_shuffle(shuffled, seed)
		letter_maps_to_itself = False
		for x in range(len(shuffled)):
			if shuffled[x] == letters[x]:
				letter_maps_to_itself = True

	substitution_map = {}
	for x in range(len(letters)):
		substitution_map[letters[x]] = shuffled[x]
	
	return substitution_map

def random_number_generator(seed):
	"""
    Input: RNG seed (integer)
    Output: pseudo-random number (integer)

    Based on the number it receives as input generates a pseudo-random number using xorshift
    """
	seed ^= ( seed << 13) & 0xFFFFFFFF
	seed ^= ( seed >> 17) & 0xFFFFFFFF
	seed ^= ( seed <<  5) & 0xFFFFFFFF
	return seed

def letter_shuffle(letters, seed):
	"""
    Input: letters (list), RNG seed (integer)
    Output: returns new seed (integer), shuffles letters received directly (list)

    Destructively alters a list of letters to rearange them in a random manner
    """
	for target in range(len(letters) - 1, 0, -1):
		seed = random_number_generator(seed)
		new_position = seed % (target + 1)
		letters[target], letters[new_position] = letters[new_position], letters[target]

	return seed

def done_using():
	print("Would you like to encrypt/decrypt another message? (Y/N)")
	while True:
		user_decision = input().upper()
		if user_decision == "Y":
			return False
		elif user_decision == "N":
			return True
		else:
			print("Please select whether or not you would like to encrypt/decrypt another message. (Y/N)")


def main():
	print("Welcome to the encryption machine V1.3")
	usage_over = False
	while not usage_over:
		message_encrypter()
		usage_over = done_using()

main()
