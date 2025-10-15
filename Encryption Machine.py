ALPHABET = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
SPECIAL_CHARACTERS = (" ", "!", "?", ".", ",", ":", "(", ")")
VALID_KEYS = ("A", "B", "C")

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
			print("Please input a valid operation: encrypt or decrypt")
			
	print("Please enter the encryption key. (Combination of {})".format(VALID_KEYS))
	while encryption_key_validity == False:	# Check encryption key composition
		encryption_key = input().upper()
		encryption_key_validity = True
		for x in encryption_key:
			if x not in VALID_KEYS:
				encryption_key_validity = False
		if encryption_key_validity == False:
			print("Please input a valid encryption key. (Combination of {})".format(VALID_KEYS))
			
	print("Please input the message.")
	while message_validity == False:
		message_validity = True
		message = input().lower()
		for x in message:
			if x not in ALPHABET and x not in SPECIAL_CHARACTERS:
				message_validity = False
		if message_validity == False:
			print("Please input a valid message.")
			
	print("Your {} message is '{}'".format(user_operation + "ed", message_shifter(operation, encryption_key, message)))


def message_shifter(operation, encryption_key, message):	# Actually encrypts or decrypts messages
	for x in encryption_key:
		letter_counter = 1
		new_message = ""
		for y in message:
			if y in SPECIAL_CHARACTERS:
				new_message = new_message + y
			else:
				old_letter_number = ALPHABET.index(y)
				if x == "A":	# Shift each letter by the position the letter occupies in the message
					new_letter_number = old_letter_number + letter_counter * operation
				elif x == "B":	# Shift each letter by the ammount of letters until the end of the message
					new_letter_number = old_letter_number + (len(message) - (letter_counter - 1)) * operation
				elif x == "C":	# Shift each letter by 2 (Caesar Cypher)
					new_letter_number = old_letter_number + 2 * operation
				
				while len(ALPHABET) - 1 < new_letter_number:
					new_letter_number = new_letter_number - len(ALPHABET)
				while new_letter_number < 0:
					new_letter_number = new_letter_number + len(ALPHABET)
				new_message = new_message + ALPHABET[new_letter_number]

			letter_counter = letter_counter + 1
		message = new_message

	return message 
	
	
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
	print("Message encrypter V1.2")
	usage_over = False
	while not usage_over:
		message_encrypter()
		usage_over = done_using()

main()
