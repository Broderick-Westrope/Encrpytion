import numpy as np
import binascii
from bitarray import bitarray


def permutation(key, indices):
    return key[indices]


def IP(bloc):
    return bloc[[1, 5, 2, 0, 3, 7, 4, 6]]


def IP_inverse(bloc):
    return bloc[[3, 0, 2, 4, 6, 1, 7, 5]]


def P4(bloc):
    return bloc[[1, 3, 2, 0]]


def EP(bloc):
    return bloc[[3, 0, 1, 2, 1, 2, 3, 0]]


def createMatrix(array):
    return np.matrix(splitIn2(array))


def xor(a, b):
    return np.logical_xor(a, b)


def switch(a):
    a, b = splitIn2(a)
    return np.concatenate([b, a])


def str2bits(n):
    result = "{0:b}".format(n)
    if (len(result) == 1):
        return "0" + result
    return result


def FK(IP, k):
    right_block = splitIn2(IP)[1]  # Take only the second half
    right_block_concatenate = np.concatenate(
        (right_block, right_block), axis=0)  # Concatenate the half to itself (making it 8 digits again)
    ep = EP(right_block_concatenate)  # Perform the E/P (extension/permutation)
    textMatrix = createMatrix(ep)  # Turn the text into a matrix
    keyMatrix = createMatrix(k)  # Turn the key into a matrix
    # Get the XOR result between the text and key matrices
    xorResults = xor(textMatrix, keyMatrix)

    # Calculate what indices need to be grabbed from S0 and S1
    indices_matrix = [0, 1, 0, 2, 0, 0, 0, 3, 1, 1, 1, 2, 1, 0, 1, 3]
    s_temp = []
    s = []

    for i in range(0, len(indices_matrix), 4):
        s_temp.append(xorResults[indices_matrix[i], indices_matrix[i + 1]] * 1)
        s_temp.append(xorResults[indices_matrix[i + 2], indices_matrix[i + 3]] * 1)

    for i in range(0, len(s_temp), 2):
        str_result = str(s_temp[i]) + str(s_temp[i + 1])
        s.append(int(str_result, 2))

    # Create the S0 and S1 matrices
    s0 = np.matrix([[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 3, 2]])
    s1 = np.matrix([[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0], [2, 1, 0, 3]])

    # Grab the correct values from S0 and S1
    a = s0[s[1], s[0]]
    b = s1[s[3], s[2]]

    # Convert it to bit values
    a = str2bits(a)
    b = str2bits(b)

    R8 = np.concatenate([np.array(bitarray(a).tolist()),
                         np.array(bitarray(b).tolist())], axis=0)
    R9 = P4(R8)
    left_block = splitIn2(IP)[0]
    R10 = xor(left_block, R9)
    R11 = np.concatenate([R10, right_block])
    return R11

#####################################################################


def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))


def text_from_bits(bits):
    return binascii.unhexlify('%x' % int('0b'+bits, 2))


def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))


# Takes the key as an array of binary and performs the P10 permutation
def permutationP10(key):
    # The order we want to grab the key values (-1 because indexing starts at 0)
    indices = [2, 4, 1, 6, 3, 9, 0, 8, 7, 5]
    key = np.array(key.tolist())  # Convert from bitarray format to a normal array
    keyP10 = key[indices]  # Using NumPy we can index key with indices values
    return keyP10


def permutationP8(key):
    indices = [5, 2, 6, 3, 7, 4, 9, 8]
    return key[indices]


# Divide two parts
def splitIn2(key):
    return np.split(key, 2)

# Circular left shift


def leftShift(key, depth):
    return np.concatenate((np.roll(key[0], depth), np.roll(key[1], depth)), 0)
