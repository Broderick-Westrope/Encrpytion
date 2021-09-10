from math import sqrt
from random import shuffle


def power(x, y, p):

    res = 1  # Initialize result

    x = x % p  # Perform x (mod p)

    while (y > 0):
        # If y is odd, multiply x with result
        if (y & 1):
            res = (res * x) % p

        # y must be even now
        y = y >> 1  # y = y/2
        x = (x * x) % p

    return res


def findPrimeFactors(n):
    s = set()

    # Print the number of 2s that divide n
    while (n % 2 == 0):
        s.add(2)
        n = n // 2

    # n must be odd at this po. So we can
    # skip one element (Note i = i +2)
    for i in range(3, int(sqrt(n)), 2):

        # While i divides n, print i and divide n
        while (n % i == 0):

            s.add(i)
            n = n // i

    # This condition is to handle the case
    # when n is a prime number greater than 2
    if (n > 2):
        s.add(n)
    return s


def findRandomPrimitive(n):  # Function to find a random primitive root of n
    # Calculates the value of the Euler Totient of n (phi). This is n-1 since n is prime.
    phi = n - 1

    # Find prime factors of phi and store in a set
    s = findPrimeFactors(phi)

    # Check for every number from 2 to phi in a random order
    candidates = range(2, phi + 1)
    print(str(candidates))
    candidates = list(candidates)
    print(str(candidates))
    shuffle(candidates)
    print(str(candidates))
    # candidates = iter(candidates)
    # print(str(candidates))
    for r in candidates:

        # Iterate through all prime factors of phi and check if we found a power with value 1
        flag = False
        for it in s:

            # Check if r^((phi)/primefactors)
            # mod n is 1 or not
            if (power(r, phi // it, n) == 1):

                flag = True
                break

        # If there was no power with value 1.
        if (flag == False):
            return r

    # If no primitive root found
    return -1


print(findRandomPrimitive(107))
