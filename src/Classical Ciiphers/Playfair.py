from string import ascii_uppercase


def Matrix(x, y, initial):
    return [[initial for i in range(x)] for j in range(y)]

 # todo Use dictionary!!!!!!!!!


matrix = Matrix(5, 5, 0)


def locateChar(c):
    pos = list()
    if c == 'J':
        c = 'I'
    for i, j in enumerate(matrix):
        for k, l in enumerate(j):
            if c == l:
                pos.append(i)
                pos.append(k)
                return pos
    print("ERROR: Could not locate " + c + " in the matrix.")


def encrypt():
    plaintext = str(input("Enter message: ")).replace(" ", "").upper()

    i = 0
    for s in range(0, len(plaintext)+1, 2):
        if s < len(plaintext)-1:
            if plaintext[s] == plaintext[s+1]:
                plaintext = plaintext[:s+1]+'X'+plaintext[s+1:]
    if len(plaintext) % 2 != 0:
        plaintext = plaintext[:]+'X'
    print("Ciphertext:", end=' ')
    while i < len(plaintext):
        loc = list()
        loc = locateChar(plaintext[i])
        loc1 = list()
        loc1 = locateChar(plaintext[i+1])

        if loc[1] == loc1[1]:
            print("{}{}".format(matrix[(loc[0]+1) % 5][loc[1]],
                  matrix[(loc1[0]+1) % 5][loc1[1]]), end='')
        elif loc[0] == loc1[0]:
            print("{}{}".format(matrix[loc[0]][(loc[1]+1) %
                  5], matrix[loc1[0]][(loc1[1]+1) % 5]), end='')
        else:
            print("{}{}".format(matrix[loc[0]][loc1[1]],
                  matrix[loc1[0]][loc[1]]), end='')
        i += 2


def decrypt():  # decryption
    msg = str(input("Enter ciphertext:")).replace(" ", "").upper()
    print("PLAIN TEXT:", end=' ')
    i = 0
    while i < len(msg):
        loc = list()
        loc = locateChar(msg[i])
        loc1 = list()
        loc1 = locateChar(msg[i+1])
        if loc[1] == loc1[1]:
            print("{}{}".format(matrix[(loc[0]-1) % 5][loc[1]],
                  matrix[(loc1[0]-1) % 5][loc1[1]]), end='')
        elif loc[0] == loc1[0]:
            print("{}{}".format(matrix[loc[0]][(loc[1]-1) %
                  5], matrix[loc1[0]][(loc1[1]-1) % 5]), end='')
        else:
            print("{}{}".format(matrix[loc[0]][loc1[1]],
                  matrix[loc1[0]][loc[1]]), end='')
        i = i+2


def generateMatrix():
    key = input("Enter key: ").replace(" ", "").upper()

    while not key.isalpha():
        print("Please enter a valid key. It must be a word or phrase with only alphabetic characters.")
        key = input("Enter key: ").replace(" ", "").upper()
    print(key)

    # Store the key first
    result = list()
    for c in key:  # storing key
        if c not in result:
            if c == 'J':
                result.append('I')
            else:
                result.append(c)

    # Store the rest of the alphabet
    flag = 0
    for i in range(65, 91):
        if chr(i) not in result:
            if i == 73 and chr(74) not in result:
                result.append("I")
                flag = 1
            elif flag == 0 and i == 73 or i == 74:
                pass
            else:
                result.append(chr(i))

    # Make the matrix
    k = 0
    for i in range(5):
        for j in range(5):
            matrix[i][j] = result[k]
            k += 1

# Starting menu


def menu():
    generateMatrix()

    while(1):
        choice = int(input("\n 1.Encryption \n 2.Decryption: \n 3.EXIT"))
        if choice == 1:
            encrypt()
        elif choice == 2:
            decrypt()
        elif choice == 3:
            exit()
        else:
            print("Choose correct choice")


menu()
