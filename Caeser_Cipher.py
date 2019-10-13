#!/usr/bin/python

from random import randint

key = randint(1,26)

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_cap = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

message = input("Enter a message: ")

newMessage = ''

for char in message:
    if char.isalpha() == True and char.islower() == True:
        position = alphabet.find(char)
        newPosition = (position + key) % 26
        newChar = alphabet[newPosition]
        newMessage += newChar
    elif char.isalpha() == True and char.isupper() == True:
        position = alphabet_cap.find(char)
        newPosition = (position + key) % 26
        newChar = alphabet_cap[newPosition]
        newMessage += newChar
    else:
        newMessage += char

print("Your encrypted message is: " + newMessage)
