import re

morse_alphabet = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----', ' ':'/'}

def encode(letter):
	return morse_alphabet[letter]

def decode(morse_letter):
	for k, v in morse_alphabet.iteritems():
		if v == morse_letter:
			return k

string = raw_input("Enter a phrase to translate: ")

output = ""

# fix determining if it's morse or english
if re.match('\-', string) != None:
	for s in string.split(" "):
		output += str(decode(s))

#if string.isalnum():
else:
	for s in string.upper():
		output += encode(s) + " "

#else:
#	for s in string.split(" "):
#		output += str(decode(s))

print output