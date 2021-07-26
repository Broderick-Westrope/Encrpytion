import math


def encrypt(_plaintext, _key):
    ctLength = float(len(_plaintext))

    # Calculate how many columns and rows the matrix needs
    col = len(_key)
    row = int(math.ceil(ctLength / col))
  
    # List of all the characters in the ciphertext
    ctList = list(_plaintext)

    # Add a filler character ($) in the empty cells
    fill_null = int((row * col) - ctLength)
    ctList.extend('$' * fill_null)
  
    # Create the matrix and insert the characters horizontally
    matrix = [ctList[i: i + col] 
              for i in range(0, len(ctList), col)]
  
    # Read the matrix vertically, in the order of the key
    keyIndex = 0
    ciphertext = ""
    keyList = sorted(list(_key))
    for _ in range(col):
        currentIndex = _key.index(keyList[keyIndex])
        ciphertext += ''.join([row[currentIndex] 
                          for row in matrix])
        keyIndex += 1
  
    return ciphertext


def decrypt(_ciphertext, _key):
    # Length of the plaintext
    ptLength = float(len(_ciphertext)) 

    # Calculate the number of columns and rows in the matrix
    col = len(_key)
    row = int(math.ceil(ptLength / col))

    # Create an empty matrix to store the plaintext
    ptMatrix = []
    for _ in range(row):
        ptMatrix += [[None] * col]
  
    # Convert the key into a sorted list so 
    # we can access the characters by their 
    # alphabetical position
    keyList = sorted(list(_key))

    # Using a new matrix, return the order of 
    # the columns to the order of the key
    k_indx = 0
    ptIndex = 0
    ptList = list(_ciphertext)
    for _ in range(col):
        currentIndex = _key.index(keyList[k_indx])
  
        for j in range(row):
            ptMatrix[j][currentIndex] = ptList[ptIndex]
            ptIndex += 1
        k_indx += 1
  
    # Convert the plaintext from a matrix to a string
    plaintext = ""
    try:
        plaintext = ''.join(sum(ptMatrix, []))
    except TypeError:
        raise TypeError("This program cannot handle repeating words.")
  
    # Remove any filler characters
    null_count = plaintext.count('$')
    if null_count > 0:
        return plaintext[: -null_count]
  
    return plaintext


def printResults(_plaintext, _ciphertext, _key):
    print("Plaintext: " + str(_plaintext))
    print("Key: " + str(_key))
    print("Ciphertext: " + str(_ciphertext))


def menu():
    choice = ' '
    while choice != 'E' and choice != 'D':
        choice = input("Would you like to [E]ncrypt or [D]ecrypt? ")

    key = "5 5"
    while not key.isalpha() and not key.isnumeric():
        key = input("Enter the keyword? (Short word or number) ").replace(" ","").upper()


    if choice == 'E':
        plaintext = input("What is the message you would like to encrypt? ").upper()
        ciphertext = encrypt(plaintext, key)
        printResults(plaintext, ciphertext, key)
    elif choice == 'D':
        ciphertext = input("What is the message you would like to decrypt? ").upper()
        plaintext = decrypt(ciphertext, key)
        printResults(plaintext, ciphertext, key)


menu()