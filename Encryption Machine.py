ALPHABET = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
SPECIAL_CHARACTERS = (" ", "!", "?", ".", ",", ":", "(", ")")
VALID_KEYS = ("A", "B", "C")

def message_encrypter():	#Setup and user input
	operation = None
	encryption_key_validity = False
	message_validity = False
	
	print("Do you want to encrypt or decrypt a message?")
	while operation != 1 and operation != -1:	#To be multiplied later so as to add or subtract letter positions 
		user_operation = input().lower()
		if user_operation == "encrypt":
			operation = 1
		elif user_operation == "decrypt":
			operation = -1
		else:
			print("Please input a valid operation: encrypt or decrypt")
			
	print("Please enter the encryption key. (Combination of {})".format(VALID_KEYS))
	while encryption_key_validity == False:	#Check encryption key composition
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
			
	message_shifter(operation, encryption_key, message)
		

def message_shifter(operation, encryption_key, message):	#Actually encrypts or decrypts messages
	for x in encryption_key:
		letter_counter = 1
		new_message = ""
		for y in message:
			if y in SPECIAL_CHARACTERS:
				new_message = new_message + y
			else:
				old_letter_number = ALPHABET.index(y)
				if x == "A":
					new_letter_number = old_letter_number + letter_counter * operation
				elif x == "B":
					new_letter_number = old_letter_number + (len(message) - (letter_counter - 1)) * operation
				elif x == "C":
					new_letter_number = old_letter_number + 2 * operation
				letter_counter = letter_counter + 1
				
				while len(ALPHABET) - 1 < new_letter_number:
					new_letter_number = new_letter_number - len(ALPHABET)
				while new_letter_number < 0:
					new_letter_number = new_letter_number + len(ALPHABET)
				new_message = new_message + ALPHABET[new_letter_number]
		message = new_message
	if operation == 1:
		operation = "encrypted"
	else:
		operation = "decrypted"
	print("Your {} message is '{}'".format(operation, message))
	go_again()
	
	
def go_again():
	decision_made = False
	print("Would you like to encrypt/decrypt another message? (Y/N)")
	while decision_made == False:
		user_decision = input().upper()
		if user_decision == "Y":
			decision_made = True
			message_encrypter()
		elif user_decision == "N":
			decision_made = True
			print("Shutting down...")
		else:
			print("Please select whether or not you would like to encrypt/decrypt another message. (Y/N)")


def main():
	print("Message encrypter V1.1")
	message_encrypter()

main()
