# Python program to find
# modular inverse of a
# under modulo m using
# Fermat's little theorem.
# This program works
# only if m is prime.


def recursiveGCD(a, b):
    if(b == 0):
        return a
    else:
        return recursiveGCD(b, a % b)


# To compute x^y under modulo m
def powerUnderMod(x, y, m):
    if (y == 0):
        return 1
    p = powerUnderMod(x, y // 2, m) % m
    p = (p * p) % m

    return p if(y % 2 == 0) else (x * p) % m


# Function to find modular
# inverse of a under modulo m
# Assumption: m is prime
def modInverse(a, m):

    if (recursiveGCD(a, m) != 1):
        print("Inverse doesn't exist")
    else:

        # If a and m are relatively prime, then
        # modulo inverse is a^(m-2) mode m
        print("Modular multiplicative inverse is ",
              powerUnderMod(a, m - 2, m))


# Driver code
a = 2**6
m = 7
modInverse(a, m)

# This code is contributed
# by Anant Agarwal.
