from encryption import *
from decryption import *
from keyGenerator import generate_k1_k2
import secrets


def main():
    key = ""
    plaintext = ""
    ciphertext = ""
    binaryText = ""

    mode = input("Would you like to [E]ncrypt or [D]ecrypt? ").replace(" ", "").upper()
    varType = input("Is it a single [B]lock or a [S]tring? ").replace(" ", "").upper()

    if mode == 'D':
        key = input("Enter the 10-bit binary key: ").replace(" ", "")
        ciphertext = input("Enter the ciphertext: ")

        if varType == "B":
            plaintext = decryptBlock(ciphertext, key)
            printBlock(plaintext, ciphertext)
        else:
            plaintext = decryptString(ciphertext, key)
            printString(plaintext, ciphertext)
    else:
        key = randomKey()
        print("Your random key is: " + key)
        plaintext = input("Enter the plaintext: ")

        if varType == "B":
            ciphertext = encryptBlock(plaintext, key)
            printBlock(plaintext, ciphertext)
        else:
            ciphertext = encryptString(plaintext, key)
            printString(text_to_bits(plaintext), ciphertext)

    print("Plaintext Key: " + key)
    keys = generate_k1_k2(key)
    print("Cyphertext Keys: " + str(keys[0])+", "+str(keys[1]))


def printBlock(plaintext, ciphertext):
    print("Ciphertext Msg: ", end='')
    printBinary(ciphertext)

    print("Plaintext Msg: ", end='',)
    printBinary(plaintext)


def printString(plaintext, ciphertext):
    print("Binary Ciphertext: ")
    printBinary(ciphertext)
    print("ASCII Ciphertext: ", end="")
    print(text_from_bits(''.join(str(e) for e in ciphertext*1)))

    print("Binary Plaintext: ", end="")
    printBinary(plaintext)
    print("ASCII Plaintext: ", end="")
    print(text_from_bits(''.join(str(e) for e in plaintext * 1)))


def randomKey():
    key = ""
    for i in range(10):
        key += str(secrets.randbelow(2))
    return key


def printBinary(code):
    print(''.join(str(e) for e in code*1))


if __name__ == "__main__":
    main()
