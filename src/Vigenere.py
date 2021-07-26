from string import ascii_uppercase

def menu():
    choice = ' '
    while choice != 'E' and choice != 'D':
        choice = input("Would you like to [E]ncrypt or [D]ecrypt? ")

    word = "5.5"
    while not word.isalpha():
        word = input("Enter the keyword? (Any word) ").upper()


    if choice == 'E':
        plaintext = input("What is the message you would like to encrypt? ").upper()
        key = generateKey(plaintext, word)
        ciphertext = encrypt(plaintext, key)
        printResults(plaintext, ciphertext, key, word)
    elif choice == 'D':
        ciphertext = input("What is the message you would like to decrypt? ").upper()
        key = generateKey(ciphertext, word)
        plaintext = decrypt(ciphertext, key)
        printResults(plaintext, ciphertext, key, word)


def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) -
                       len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))


def encrypt(string, key):
    cipher_text = []
    for i in range(len(string)):
        x = (ord(string[i]) +
             ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return("" . join(cipher_text))


def decrypt(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) -
             ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return("" . join(orig_text))


def printResults(_plaintext, _ciphertext, _key, _word):
        print("Plaintext: " + str(_plaintext))
        print("Key: " + str(_key))
        print("Keyword: " + str(_word))
        print("Ciphertext: " + str(_ciphertext))

menu()