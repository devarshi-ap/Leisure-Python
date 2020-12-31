# Prime Factorization

factors = lambda n: [x for x in range(1, n + 1) if not n % x]
isPrime = lambda n: len(factors(n)) == 2
primefactors = lambda n: list(filter(isPrime, factors(n)))


def primeFactorize(n):
    n = int(n)
    f = primefactors(n)
    if isPrime(n):
        return str(n)
    else:
        return str(f[0]) + "*" + primeFactorize(n / f[0])


print("Welcome to the Prime Factorizer\nEnter a number or enter 'quit' to exit")
num = 0;

while True:
    if num:
        print(primeFactorize(num))
    print(">>>", end='')
    num = input()
    if num == "quit":
        break
