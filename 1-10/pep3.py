# We define the "prime factors function" that return the prime factors of a number. We have to define the function that return bool value if a number is prime or not.

import time

def is_prime(n):
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(n**0.5)+1, 2):
            if n % i == 0:
                return False
        return True

def prime_factors_of_n(n):
    prime_factors = []
    for i in range(2, int(n**0.5)+1):
        if n % i == 0 and is_prime(i):
            prime_factors.append(i)
    return prime_factors

if __name__ == "__main__":
    start = time.time()
    print(max(prime_factors_of_n(600851475143)))
    print(time.time() - start)

#It was very slow to find the prime factors of 600851475143. We can find a better solution but it was satisfying in this case.