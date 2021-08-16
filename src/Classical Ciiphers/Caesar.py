import math
from random import randint


def encrypt(_text, _key):
    result = ""

    for i in range(len(_text)):
        char = _text[i]

        if (char.isupper()):
            result += chr((ord(char) + _key-65) % 26 + 65)
        else:
            result += chr((ord(char) + _key - 97) % 26 + 97)

    return result


def decrypt(_text, _key):
    result = ""

    for i in range(len(_text)):
        char = _text[i]

        if (char.isupper()):
            result += chr((ord(char) - _key-65) % 26 + 65)
        else:
            result += chr((ord(char) - _key - 97) % 26 + 97)

    return result


def printResults(_plaintext, _ciphertext, _key):
    print("Plaintext: " + str(_plaintext))
    print("Key: " + str(_key))
    print("Ciphertext: " + str(_ciphertext))


def menu():
    choice = ' '
    while choice != 'E' and choice != 'D':
        choice = input("Would you like to [E]ncrypt or [D]ecrypt? ")

    key = 5.5
    while True:
        val = input("Enter the key? (0-25) ")
        if(val == "R"):
            key = randint(0, 25)
            break
        else:
            try:
                key = int(val)
                key = math.floor(key)
                while key < 0:
                    key += 26
                while key > 25:
                    key -= 26
                break
            except ValueError:
                print("Please enter a number between 0 and 25 (inclusive).")

    if choice == 'E':
        plaintext = input("What is the message you would like to encrypt? ").replace(
            " ", "").upper()
        ciphertext = encrypt(plaintext, key)
        printResults(plaintext, ciphertext, key)
    elif choice == 'D':
        ciphertext = input("What is the message you would like to decrypt? ").replace(
            " ", "").upper()
        plaintext = decrypt(ciphertext, key)
        printResults(plaintext, ciphertext, key)


if __name__ == "__main__":
    menu()
