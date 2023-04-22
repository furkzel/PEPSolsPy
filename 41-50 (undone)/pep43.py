"""from itertools import permutations
import time 

def pandigital_nums(n):
    I = [int(''.join(p)) for p in permutations('123456789'[:n])]
    return I

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

def main():
    nine_digits_pandigital_nums = pandigital_nums(9)
    primes = sieve_of_Eratosthenes(1000)

    for t in primes:
        for i in nine_digits_pandigital_nums:
            I = []
            for k in range(1, 8):
                if int(str(i)[k:k+3]) % t == 0:
                    I.append(t)

            if len(I) == 7:
                print(i)
                break
    
if __name__ == '__main__':
    start = time.time()
    main()
    print(time.time() - start)
"""

from itertools import permutations
import time 

def pandigital_nums(n):
    for p in permutations('1234567890'[:n]):
        yield int(''.join(p))

primes = [2, 3, 5, 7, 11, 13, 17]

def is_substring_divisible(num):
	return all((num[i + 1] * 100 + num[i + 2] * 10 + num[i + 3]) % p == 0
		for (i, p) in enumerate(primes))

def main():
	ans = sum(int("".join(map(str, num)))
		for num in permutations(list(range(10)))
		if is_substring_divisible(num))
	return int(str(ans))

if __name__ == '__main__':
    start = time.time()
    main()
    print(time.time() - start)                                          
