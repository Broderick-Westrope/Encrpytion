def main():
    print("** NOTE: All numbers must be non-negative, whole numbers **")

    while True:
        a = input("Enter the first number (base): ").replace(" ", "")
        if(a.isdigit()):
            a = int(a)
            break
        else:
            print("** ERROR: All numbers must be non-negative, whole numbers **")

    while True:
        b = input("Enter the second number (modulus): ")
        if(b.isdigit()):
            b = int(b)
            break
        else:
            print("** NOTE: All numbers must be non-negative, whole numbers **")

    biggest = max(a, b)
    relativePrimes = calculateRelativePrimes(biggest)

    print("GCD: " + str(iterativeGCD(a, b)))
    print("Multiplicative Inverse: " + str(calculateMultiplicativeInverse(a, b)))
    print("Euler's Totient: " + str(len(relativePrimes)))
    print("Z* (relative primes) of " + str(biggest) + ": " + str(relativePrimes))


def iterativeGCD(a, b):
    A, B = a, b
    while(B >= 0):
        if(B == 0):
            return A
        R = A % B
        A = B
        B = R


def calculateMultiplicativeInverse(b, m):
    A1, A2, A3 = 1, 0, m
    B1, B2, B3 = 0, 1, b
    print("1.&\ (A1,A2,A3):=(1,0," + str(m) + "); (B1,B2,B3):=(0,1," + str(b) + ") \\\\")
    while(B3 > 0):
        print("2.&\ B3=" + str(B3) + "\\\\")
        if(B3 == 1):
            print("3.&\ B3=1. B2=" + str(B2) + "\\\\")
            while(B2 < 0):
                B2 += m
            return B2
        else:
            print("3.&\ B3=" + str(B3) + "\\\\")
        Q = A3 // B3
        print("4.&\ Q := A3//B3 = " + str(A3) + "//" + str(B3) + " = " + str(Q) + "\\\\")
        T1, T2, T3 = (A1-Q*B1), (A2-Q*B2), (A3-Q*B3)
        # (A1-Q*B1, A2-Q*B2, A3-Q*B3) =
        print("5.&\ (T1, T2, T3) :=  (" + str(A1) + "-"+str(Q)+"*" + str(B1) + ", " + str(A2)+"-"+str(Q)+"*"+str(B2) +
              ", " + str(A3)+"-"+str(Q)+"*"+str(B3)+") = (" + str(A1-Q*B1) + ", " + str(A2-Q*B2) + ", " + str(A3-Q*B3) + ") \\\\")
        A1, A2, A3 = B1, B2, B3
        print("6.&\ (A1, A2, A3) := (B1, B2, B3) = (" +
              str(B1) + ", " + str(B2) + ", " + str(B3) + ") \\\\")
        B1, B2, B3 = T1, T2, T3
        print("7.&\ (B1, B2, B3) := (T1, T2, T3) = (" +
              str(T1) + ", " + str(T2) + ", " + str(T3) + ") \\\\")
    print("2.&\ B3=0. No inverse. \\")
    return ("There is no multiplicative inverse for " + str(m) + " and " + str(b) + ". \\\\")


def calculateRelativePrimes(x):
    relativePrimes = []
    for i in range(1, x):
        if iterativeGCD(i, x) is 1:
            relativePrimes.append(i)
    return relativePrimes


if __name__ == "__main__":
    main()
