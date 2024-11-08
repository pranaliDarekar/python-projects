# Encryption program

import random
import string

char = " " + string.punctuation + string.digits + string.ascii_letters
char = list(char)
key = char.copy()

random.shuffle(key)

#print(f"char: {char}")
#print(f"key : {key}")

#Encryption

og_message = input("Enter a message: ")
cipher_text = ""

for letter in og_message:
    index = char.index(letter)
    cipher_text += key[index]

print(f"original text: {og_message}")
print(f"encrypted text: {cipher_text}")


# Decryption
cipher_text = input("Enter a cryptic message: ")
og_message = ""

for letter in cipher_text:
    index = key.index(letter)
    og_message += char[index]

print(f"encrypted text: {cipher_text}")
print(f"original text: {og_message}")