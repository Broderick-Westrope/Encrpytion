from random import randint
from GetPrime import getNBitPrime
from PrimitiveRoot import findRandomPrimitive


def generateValues():
    while True:
        p = getNBitPrime(8)
        g = findRandomPrimitive(p)
        if(g != -1):
            break
    Xa, Xb = randint(2, p-1), randint(2, p-1)

    Ya = g**Xa  # ! Change this to use SAM (Square and multiply)
    Ya %= p

    Yb = g**Xb  # ! Change this to use SAM (Square and multiply)
    Yb %= p

    Ka = Yb**Xa
    Ka %= p

    Kb = Ya**Xb
    Kb %= p

    assert Ka == Kb
    return(p, g, Xa, Xb, Ya, Yb, Ka)


def printValues(p, g, Xa, Xb, Ya, Yb, K):
    print("p:\t", p)
    print("g:\t", g)
    print("Xa:\t", Xa)
    print("Xb:\t", Xb)
    print("Ya:\t", Ya)
    print("Yb:\t", Yb)
    print("K:\t", K)


if __name__ == '__main__':
    p, g, Xa, Xb, Ya, Yb, K = generateValues()
    printValues(p, g, Xa, Xb, Ya, Yb, K)
