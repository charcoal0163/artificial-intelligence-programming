# lab manual 4 - functions
# activity 1 - sum of numbers
def sumToN(n):
    f = 0
    if n == 0:
        return 0
    else:
        i = 0
        while (i <= n):
            if (i % 3 == 0):
                pass
            else:
                f += i
                if (f >= 50):
                    return f
            i += 1
        return f

n = int(input("Enter an upper bound for the summation: "))
print(sumToN(n))

# activity 2 - series (approximate pi)
def displayPi(i):
    frac = 0
    sumed = 0
    while True:
        top = ((-1) ** (i + 1))
        bottom = ((2 * i) - 1)
        frac = top / bottom
        i -= 1
        sumed += frac
        if (i == 0):
            break
    return 4 * (sumed)

i = int(input("Enter value of i: "))
pi = displayPi(i)
print(pi)

# activity 3 - prime numbers
def isPrime(x):
    if x <= 1:
        return False
    for i in range(2, x + 1):
        if x % i == 0:
            return False
        else:
            return True
def primes(a, b):
    for i in range(a, b + 1):
        if isPrime(i):
            print(i)
        
primes(1, 15)
