# prime factorization

def isPrime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


userNum = int(input("Prime Factorization\n\nEnter a number to find all prime factors: "))
primeFactors = []

for i in range(1,userNum+1):
    if userNum % i == 0 and isPrime(i):
        primeFactors.append(i)

print("Here are all the prime factors of {}: \t{}".format(userNum, primeFactors))
