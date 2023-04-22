from itertools import permutations

def pandigital_nums(n):
    I = [int(''.join(p)) for p in permutations('123456789'[:n])]
    return I

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

def main():
    results = []
    for i in pandigital_nums(7):
        if is_prime(i):
            results.append(i)
        
    print(max(results))

if __name__ == '__main__':
    main()
