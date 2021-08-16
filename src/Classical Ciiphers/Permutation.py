def main():
    while True:  # Get the permutation order
        P = input("Enter the permutation: ").replace(" ", "").upper()
        if(checkP(P)):
            break
        else:
            print("** ERROR: Permutation must include all numbers from 1 up to the length of the permutation (ie. 32541) **")
    while True:  # Get the plaintext
        inputV = input("Enter the text: ")
        if(len(P) == len(inputV)):
            break
        else:
            print("** ERROR: The input must be the same length as the permutation. **")
    while True:  # Get the mode we are doing
        mode = input("Do you want to [E]ncrypt or [D]ecrypt? ").replace(" ", "").upper()
        if(mode == 'D'):
            output = encrypt(inverseP(P), inputV)
            printValues(P, output, inputV)
            break
        elif(mode == 'E'):
            output = encrypt(P, inputV)
            printValues(P, inputV, output)
            break
        else:
            print("** ERROR: Invalid input. **")


def inverseP(P):
    result = ""
    for n in range(1, len(P)+1):
        result += str(P.index(str(n)) + 1)
    return result


def encrypt(P, plaintext):
    result = ""
    for i in range(0, len(P)):
        result += plaintext[int(P[i])-1]
    return result


def checkP(P):
    return all(str(val + 1) in P for val in range(len(P)))


def printValues(P, plaintext, ciphertext):
    print("Plaintext: " + str(plaintext))
    print("P: " + str(P))
    print("Ciphertext: " + str(ciphertext))


if __name__ == '__main__':
    main()
