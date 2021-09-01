def theSieve(n):
    '''# Finds all primes less than or equal to n using the Sieve of Eratosthenes'''

    # Create a boolean array
    # "prime[0..n]" and initialize
    # all entries it as true.
    # A value in prime[i] will
    # finally be false if i is
    # Not a prime, else true.
    prime = [True for i in range(n+1)]
    p = 2
    results = []
    while (p * p <= n):

        # If prime[p] is not
        # changed, then it is a prime
        if (prime[p] == True):

            # Update all multiples of p
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1

    # Add all prime numbers to our list
    for p in range(2, n+1):
        if prime[p]:
            # print(p)
            results.append(p)
    return results


# Driver code
if __name__ == '__main__':
    n = 1000
    print("Following are the prime numbers smaller than or equal to", n)
    print(str(theSieve(n)))
