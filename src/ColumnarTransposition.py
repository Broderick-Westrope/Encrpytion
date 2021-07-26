import math


def encrypt(_plaintext, _key):
    cipher = ""
  
    # track key indices
    k_indx = 0
  
    msg_len = float(len(_plaintext))
    msg_lst = list(_plaintext)
    key_lst = sorted(list(_key))
  
    # Calculate how many columns the matrix needs
    col = len(_key)

    # Calculate how many rows the matrix needs
    row = int(math.ceil(msg_len / col))
  
    # Add a filler character ($) in the empty cells
    fill_null = int((row * col) - msg_len)
    msg_lst.extend('$' * fill_null)
  
    # Create the matrix and insert the characters horizontally
    matrix = [msg_lst[i: i + col] 
              for i in range(0, len(msg_lst), col)]
  
    # Read the matrix vertically, in the order of the key
    for _ in range(col):
        curr_idx = _key.index(key_lst[k_indx])
        cipher += ''.join([row[curr_idx] 
                          for row in matrix])
        k_indx += 1
  
    return cipher


def decrypt(_ciphertext, _key):
    msg = ""
  
    # track key indices
    k_indx = 0
  
    # track msg indices
    msg_indx = 0
    msg_len = float(len(_ciphertext))
    msg_lst = list(_ciphertext)
  
    # calculate column of the matrix
    col = len(_key)
      
    # calculate maximum row of the matrix
    row = int(math.ceil(msg_len / col))
  
    # convert key into list and sort 
    # alphabetically so we can access 
    # each character by its alphabetical position.
    key_lst = sorted(list(_key))
  
    # create an empty matrix to 
    # store deciphered message
    dec_cipher = []
    for _ in range(row):
        dec_cipher += [[None] * col]
  
    # Arrange the matrix column wise according 
    # to permutation order by adding into new matrix
    for _ in range(col):
        curr_idx = _key.index(key_lst[k_indx])
  
        for j in range(row):
            dec_cipher[j][curr_idx] = msg_lst[msg_indx]
            msg_indx += 1
        k_indx += 1
  
    # convert decrypted msg matrix into a string
    try:
        msg = ''.join(sum(dec_cipher, []))
    except TypeError:
        raise TypeError("This program cannot",
                        "handle repeating words.")
  
    null_count = msg.count('_')
  
    if null_count > 0:
        return msg[: -null_count]
  
    return msg


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