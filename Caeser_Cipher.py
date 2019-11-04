#!/usr/bin/python

key = 3

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_cap = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def scramble(message):
    newMessage = ''
    for char in message:
        if char.isalpha() == True and char.islower() == True:
            newPosition = (alphabet.find(char) + key) % 26
            newMessage += alphabet[newPosition]
        elif char.isalpha() == True and char.isupper() == True:
            newPosition = (alphabet_cap.find(char) + key) % 26
            newMessage += alphabet_cap[newPosition]
        else:
            newMessage += char

    print("Your encrypted message is: " + newMessage)

scramble("Hello, my name is Rishi.")
