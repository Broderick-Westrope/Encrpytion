import numpy as np


def encrypt(plaintext):
    # Replace spaces with nothing
    plaintext = plaintext.replace(" ", "")
    # Ask for keyword and get encryption matrix
    K = makeKey()
    # Append zero if the messsage isn't divisble by 2
    len_check = len(plaintext) % 2 == 0
    if not len_check:
        plaintext += "0"
    # Populate message matrix
    P = generateMatrix(plaintext)
    # Calculate length of the message
    msg_len = int(len(plaintext) / 2)
    # Calculate P * C
    encrypted_msg = ""
    for i in range(msg_len):
        # Dot product
        row_0 = P[0][i] * K[0][0] + P[1][i] * K[0][1]
        # Modulate and add 65 to get back to the A-Z range in ascii
        integer = int(row_0 % 26 + 65)
        # Change back to chr type and add to text
        encrypted_msg += chr(integer)
        # Repeat for the second column
        row_1 = P[0][i] * K[1][0] + P[1][i] * K[1][1]
        integer = int(row_1 % 26 + 65)
        encrypted_msg += chr(integer)
    return encrypted_msg

def decrypt(ciphertext):
    # Ask for keyword and get encryption matrix
    C = makeKey()
    # Inverse matrix
    determinant = C[0][0] * C[1][1] - C[0][1] * C[1][0]
    determinant = determinant % 26
    multiplicative_inverse = findMultiplicativeInverse(determinant)
    C_inverse = C
    # Swap a <-> d
    C_inverse[0][0], C_inverse[1][1] = C_inverse[1, 1], C_inverse[0, 0]
    # Replace
    C[0][1] *= -1
    C[1][0] *= -1
    for row in range(2):
        for column in range(2):
            C_inverse[row][column] *= multiplicative_inverse
            C_inverse[row][column] = C_inverse[row][column] % 26

    P = generateMatrix(ciphertext)
    msg_len = int(len(ciphertext) / 2)
    decrypted_msg = ""
    for i in range(msg_len):
        # Dot product
        column_0 = P[0][i] * C_inverse[0][0] + P[1][i] * C_inverse[0][1]
        # Modulate and add 65 to get back to the A-Z range in ascii
        integer = int(column_0 % 26 + 65)
        # Change back to chr type and add to text
        decrypted_msg += chr(integer)
        # Repeat for the second column
        column_1 = P[0][i] * C_inverse[1][0] + P[1][i] * C_inverse[1][1]
        integer = int(column_1 % 26 + 65)
        decrypted_msg += chr(integer)
    if decrypted_msg[-1] == "0":
        decrypted_msg = decrypted_msg[:-1]
    return decrypted_msg

def findMultiplicativeInverse(determinant):
    multiplicative_inverse = -1
    for i in range(26):
        inverse = determinant * i
        if inverse % 26 == 1:
            multiplicative_inverse = i
            break
    return multiplicative_inverse

# Turn the given 4-letter key into a 2x2 matrix
def makeKey():
     # Make sure cipher determinant is relatively prime to 26 and only a/A - z/Z are given
    determinant = 0
    K = None
    while True:
        key = input("Input 4 letter key: ").replace(" ","").upper()
        K = generateMatrix(key)
        determinant = K[0][0] * K[1][1] - K[0][1] * K[1][0]
        determinant = determinant % 26
        print("The determinant is "+ str(determinant))
        inverse_element = findMultiplicativeInverse(determinant)
        if inverse_element == -1:
            print("The determinant " + str(determinant) + " is not relatively prime to 26, making the key uninvertible.")
        elif np.amax(K) > 26 or np.amin(K) < 0:
            print("Only A-Z characters are accepted")
            print(np.amax(K), np.amin(K))
        else:
            break
    return K

def generateMatrix(string):
    # Map string to a list of integers A <-> 0, B <-> 1 ... Z <-> 25
    integers = [(ord(c) - 65) for c in string]
    length = len(integers)
    M = np.zeros((2, int(length / 2)), dtype=np.int32)
    iterator = 0
    for column in range(int(length / 2)):
        for row in range(2):
            M[row][column] = integers[iterator]
            iterator += 1
    return M

if __name__ == "__main__":
    plaintext = input("What message would you like to encrypt? ").replace(" ","").upper()

    ciphertext = encrypt(plaintext)
    print(ciphertext)

    ciphertext = decrypt(ciphertext)
    print(ciphertext)