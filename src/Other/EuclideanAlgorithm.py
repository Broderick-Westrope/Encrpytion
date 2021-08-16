def main():
    print("** NOTE: All numbers must be non-negative, whole numbers **")

    while True:
        a = input("Enter the first number: ").replace(" ", "")
        if(a.isdigit()):
            break
        else:
            print("** ERROR: All numbers must be non-negative, whole numbers **")

    while True:
        b = input("Enter the second number: ")
        if(b.isdigit()):
            break
        else:
            print("** NOTE: All numbers must be non-negative, whole numbers **")

    print("GCD: " + str(calculateGCD(int(a), int(b))))
    print("Multiplicative Inverse: " + str(calculateMultiplicativeInverse(int(a), int(b))))


def calculateGCD(a, b):
    A, B = a, b
    while(B >= 0):
        if(B == 0):
            return A
        R = A % B
        A = B
        B = R


def calculateMultiplicativeInverse(m, b):
    A1, A2, A3 = 1, 0, m
    B1, B2, B3 = 0, 1, b
    while(B3 > 0):
        if(B3 == 1):
            while(B2 < 0):
                B2 += m
            return B2
        Q = A3 // B3
        T1, T2, T3 = (A1-Q*B1), (A2-Q*B2), (A3-Q*B3)
        A1, A2, A3 = B1, B2, B3
        B1, B2, B3 = T1, T2, T3
    return ("There is no multiplicative inverse for " + str(m) + " and " + str(b) + ".")


if __name__ == "__main__":
    main()
