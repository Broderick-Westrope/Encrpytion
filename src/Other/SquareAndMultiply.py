# Basic function highlighting a simple approach to solving large 
# powers using the SAM (Square and Multiply) method

def SAM(base, power):
    # x^0 = 1
    if not power: return 1
    # x^1 = x
    if power == 1: return base
    
    if power % 2:
        return base * SAM(base**2, (power-1)/2)
    else:
        return SAM(base**2,power/2)

base = int(input('Enter base: '))
power = int(input('Enter power: '))
print('Result using SAM: ' + str(SAM(base, power)))
print('Result using basic math: ' + str(base**power))