import KeyGeneration.GetPrime as getPrime
from Utils import iterativeGCD, calculateMultiplicativeInverse, SAM, calculatePhiN
from random import choice


def generateValues():
    p, q, n, e, d = 0, 0, 0, 0, 0
    while True:
        p = getPrime.getNBitPrime(8)
        print("P:\t", p)
        q = getPrime.getNBitPrime(8)
        print("Q:\t", q)
        if(p != q):
            break
    n = p * q
    phiN = ((p-1)*(q-1))
    print("N:\t", n)
    print("Phi(N):\t", phiN)
    while True:
        e = choice(range(2, phiN))
        if(iterativeGCD(e, phiN) == 1):
            break
    print("E:\t", e)
    d = calculateMultiplicativeInverse(e, calculatePhiN(n))
    print("D:\t", d)

    return(n, e, d)


def convert(base, exponent, mod):
    # Use square and multiply
    en = SAM(base, exponent)
    c = en % mod
    return c


def menu():
    n, e, d = 0, 0, 0
    val = input("Use Random Values? [Y/N]")
    if(val == "Y" or val == "y"):
        n, e, d = generateValues()
    else:
        while True:
            n = input("Enter n: ")
            e = input("Enter e: ")
            d = input("Enter d: ")
            try:
                n = int(n)
                assert n > 0
                e = int(e)
                assert e > 0
                d = int(d)
                assert d > 0
                break
            except ValueError:
                print("Please enter all positive numbers.")

    pt = int(input("Enter message: "))
    ct = convert(pt, e, n)
    # pt = convert(convert(ct, e, n), d, n)
    pt = convert(ct, d, n)
    print("Encrypted message:\t", ct)
    print("Decrypted message:\t", pt)


if __name__ == '__main__':
    menu()
