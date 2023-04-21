# We can absouetly use the is_prime function for this probleme but we can solve this efficently with the sieve of Eratosthenes.

import time
"""
def sieve_of_Eratosthenes(n):
    primes =  [True for i in range(n+1)] #we create a list of boolean values
    result_primes = []
    p = 2 #initial value of p
    while (p * p <= n):
        if (primes[p] == True):
            for i in range(p * 2, n+1, p):
                primes[i] = False
        p += 1

    for p in range(2, n+1):
        if primes[p]:
            result_primes.append(p)

    return result_primes

len(sieve_of_Eratosthenes(10000))
"""

def main():
    primes = [2]

    i = 3

    while len(primes) < 10001:
        for j in primes:
            if i % j == 0:
                break
        else:
            primes.append(i)
        i += 2

    return primes[10001 - 1]


if __name__ == "__main__":
    start = time.time()
    main()
    print(time.time() - start)
