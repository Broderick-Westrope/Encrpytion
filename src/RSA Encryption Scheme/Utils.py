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
    while(B3 > 0):
        if(B3 == 1):
            while(B2 < 0):
                B2 += m
            return B2
        else:
            Q = A3 // B3
        T1, T2, T3 = (A1-Q*B1), (A2-Q*B2), (A3-Q*B3)
        # (A1-Q*B1, A2-Q*B2, A3-Q*B3) =
        A1, A2, A3 = B1, B2, B3
        B1, B2, B3 = T1, T2, T3
    return ("There is no multiplicative inverse for " + str(m) + " and " + str(b) + ". \\\\")


def SAM(base, power):
    # print(base, "^", power)

    # x^0 = 1
    if not power:
        return 1
    # x^1 = x
    if power == 1:
        return base

    if power % 2:
        return base * SAM(base**2, (power-1)/2)
    else:
        return SAM(base**2, power/2)


def calculatePhiN(x):
    relativePrimes = []
    for i in range(1, x):
        if iterativeGCD(i, x) is 1:
            relativePrimes.append(i)
    return len(relativePrimes)
