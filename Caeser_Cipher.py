#!/usr/bin/python

key = 3

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_cap = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def scramble(message):
    newMessage = ''
    for char in message:
        if char.isalpha() and char.islower():
            newPosition = (alphabet.find(char) + key) % 26
            newMessage += alphabet[newPosition]
        elif char.isalpha() and char.isupper():
            newPosition = (alphabet_cap.find(char) + key) % 26
            newMessage += alphabet_cap[newPosition]
        else:
            newMessage += char

    print("Your encrypted message is: " + newMessage)

scramble("Hello, my name is Rishi.")
