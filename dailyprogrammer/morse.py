#daily programmer easy challenge 7

morse_alphabet = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----', ' ':'/'}
reverse_alphabet = dict((v,k) for (k,v) in morse_alphabet.items())

def encode(letter):
	return morse_alphabet[letter]

def decode(morse_letter):
	return reverse_alphabet[morse_letter]

string = raw_input("Enter a phrase to translate: ")

output = ""

if ('-' in string) or ('.' in string):
	for s in string.split(" "):
		output += str(decode(s))

else:
	for s in string.upper():
		output += encode(s) + " "

print output