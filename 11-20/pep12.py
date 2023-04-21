import time

def triangle_number_generator(nth):
    result = 0

    for i in range(1, nth+1):
        result += i
    
    return result

def number_of_divisors(number):
    count = 0

    for i in range(1, number+1):
        if number % i == 0:
            count += 1
    
    return count

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

def number_of_divisors_of_n(n):
    primes = []

    for i in prime_factors_of_n(n):
        count = 0
        while n % i == 0:
            count += 1
            n = n // i
        primes.append((i, count))

    result = 1

    for i in primes:
        result *= (i[1] + 1)

    return result

def main():
    i = 1
    while True:
        if number_of_divisors_of_n(triangle_number_generator(i)) > 500:
            return triangle_number_generator(i)
        i += 1
    
if __name__ == "__main__":
    start = time.time()
    print(main())
    print(time.time() - start)
    