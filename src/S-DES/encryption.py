from keyGenerator import *

# Encrypts a string of 8 binary characters


def encryptBlock(block, key):
    k1, k2 = generate_k1_k2(key)  # Generate the encrypted key in two halves
    # Convert the string to bit array, then bot array to a standard array
    plaintext = np.array(bitarray(block).tolist())
    plaintextIP = IP(plaintext)  # Run the initial permutation

    # Using the first half of the key, perform the complex FK funcion
    Fk_K1 = FK(plaintextIP, k1)

    swapped = switch(Fk_K1)  # Swap the LHS and RHS

    # Perform the complex FK function now with the second half of the key
    Fk_K2 = FK(swapped, k2)

    return IP_inverse(Fk_K2)  # Perform the P-inverse function


# Encrypt a string of ASCII characters


def encryptString(message, key):
    result = np.array([], dtype=bool)
    for character in message:
        binaryChar = text_to_bits(character)
        test = encryptBlock(binaryChar, key)
        result = np.concatenate((result, test), axis=0)
    return result
