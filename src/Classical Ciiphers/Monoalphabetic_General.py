from string import ascii_uppercase


def menu():
    choice = ' '
    while choice != 'E' and choice != 'D':
        choice = input("Would you like to [E]ncrypt or [D]ecrypt? ")

    interval = "a"
    while not interval.isnumeric():
        interval = input("Enter the number of columns? (1-26) ").upper()

    key = makeKey(int(interval))

    if choice == 'E':
        plaintext = input("What is the message you would like to encrypt? ")
        ciphertext = translateMessage(plaintext, key,choice)
        printResults(plaintext, ciphertext, key, interval)
    elif choice == 'D':
        ciphertext = input("What is the message you would like to decrypt? ")
        plaintext = translateMessage(ciphertext, key, choice)
        printResults(plaintext, ciphertext, key, interval)


def makeKey(_interval):
    letters=[]
    letters[:0] = ascii_uppercase
    key = ""
    loops = 26
    i = 0
    resets = 0
    while loops > 0:
        key += letters[i]
        i += _interval
        loops -= 1
        if(i >= 26):
            resets+=1
            i = resets
    return key


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

def printResults(_plaintext, _ciphertext, _key, _interval):
        print("Plaintext: " + str(_plaintext))
        print("Key: " + str(_key))
        print("Interval: " + str(_interval))
        print("Ciphertext: " + str(_ciphertext))

menu()