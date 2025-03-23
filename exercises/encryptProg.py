import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

#gets characters
#puts characters into a list
#defines "key" and its just also the characters

#print(f"chars: {chars}")
#print(f"key:{key}")

#ENCRYPT
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"original message: {plain_text}")
print(f"encrypted message: {cipher_text}")

#Gets an input from the user
#defines cipher text as blank for now
#iterates through the user message, finding the index of each character
#makes cipher text by finding the position of the char, and typing the corresponding position in the shuffled key


#DECRYPT
cipher_text = input("Enter a message to encrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"original message: {plain_text}")
print(f"encrypted message: {cipher_text}")