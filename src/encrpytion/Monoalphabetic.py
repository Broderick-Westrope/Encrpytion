import sys, random
from string import ascii_uppercase


def menu():
    choice = ' '
    while choice != 'E' and choice != 'D':
        choice = input("Would you like to [E]ncrypt or [D]ecrypt? ")

    key = "5.5"
    while not key.isalpha():
        key = input("Enter the key? (A word) ").upper()

    key = "".join(dict.fromkeys(key+ ascii_uppercase))
    checkValidKey(key)

    if choice == 'E':
        plaintext = input("What is the message you would like to encrypt? ")
        ciphertext = translateMessage(plaintext, key,choice)
        printResults(plaintext, ciphertext, key)
    elif choice == 'D':
        ciphertext = input("What is the message you would like to decrypt? ")
        plaintext = translateMessage(ciphertext, key, choice)
        printResults(plaintext, ciphertext, key)


def checkValidKey(key):
    keyList = list(key)
    lettersList = list(ascii_uppercase)
    keyList.sort()
    lettersList.sort()
    if keyList != lettersList:
        sys.exit('There is an error in the key or symbol set.')


def translateMessage(message, key, mode):
    translated = ''
    charsA = ascii_uppercase
    charsB = key
    if mode == 'D':
        charsA, charsB = charsB, charsA

    print(str(len(charsA)))
    print(str(len(charsB)))

    for symbol in message:
        if symbol.upper() in charsA:
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            translated += symbol

    return translated

def printResults(_plaintext, _ciphertext, _key):
        print("Plaintext: " + str(_plaintext))
        print("Key: " + str(_key))
        print("Ciphertext: " + str(_ciphertext))


menu()