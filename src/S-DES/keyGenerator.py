from bitarray import bitarray
from functions import *

# Takes in a key as a String and returns the two halves of the encrypted key


def generate_k1_k2(key):
    ba = bitarray(key)  # Turn the string of binary into an array
    P10 = permutationP10(ba)  # Perform P10
    split = splitIn2(P10)  # Split the key in two
    # Shift both portions of the key left by 1 (individually)
    LS1 = leftShift(split, -1)
    k1 = permutationP8(LS1)  # Perform P8, giving us the first half of the key
    split = splitIn2(LS1)  # Split the key (again)
    # Shift both portions of the key left by 2 (individually)
    LS2 = leftShift(split, -2)
    k2 = permutationP8(LS2)  # Perform P8, giving us the second half of the key
    return(k1, k2)
