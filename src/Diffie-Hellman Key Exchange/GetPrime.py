from random import randrange


# The primes <= 1000 generated using the Eratosthenes Sieve
firstPrimesList = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479,
                   487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]


def getPrimeCandidate(n):
    ''' Used to pick a large odd number which has potential to be our prime'''
    return(randrange(2**(n-1)+1, 2**n-1))


# This step is a low-level primality test which requires the pre-calculation of the first few hundred primes (done using Sieve of Eratosthenes)
def getLowLevelPrime(n):
    '''Generate a prime candidate divisible
    by first primes'''

    # Repeat until a number satisfying the test is found
    while True:

        # Obtain a random number as our candidate
        primeCandidate = getPrimeCandidate(n)

        for divisor in firstPrimesList:
            if primeCandidate % divisor == 0 and divisor**2 <= primeCandidate:
                break
            # If no divisor found, return value
            else:
                return primeCandidate


# This step is a high-level primality test that automatically runs 20 iterations of itself
def isMillerRabinPassed(miller_rabin_candidate):
    '''Runs 20 iterations of Rabin Miller Primality test'''

    maxDivisionsByTwo = 0
    evenComponent = miller_rabin_candidate-1

    while evenComponent % 2 == 0:
        evenComponent >>= 1
        maxDivisionsByTwo += 1
    assert(2**maxDivisionsByTwo * evenComponent == miller_rabin_candidate-1)

    def trialComposite(round_tester):
        if pow(round_tester, evenComponent, miller_rabin_candidate) == 1:
            return False

        for i in range(maxDivisionsByTwo):
            if pow(round_tester, 2**i * evenComponent, miller_rabin_candidate) == miller_rabin_candidate-1:
                return False
        return True

    # Set number of trials here
    numberOfRabinTrials = 20
    for i in range(numberOfRabinTrials):
        round_tester = randrange(2, miller_rabin_candidate)

    if trialComposite(round_tester):
        return False
    return True


def getNBitPrime(n):
    while True:
        primeCandidate = getLowLevelPrime(n)
        if not isMillerRabinPassed(primeCandidate):
            continue
        else:
            return primeCandidate
            break


if __name__ == '__main__':
    print("1024-bit prime is: ")
    print(getNBitPrime(1024))
