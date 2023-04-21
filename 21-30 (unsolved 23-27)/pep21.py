import time

def divisors_of_n(n):
    result = []
    for i in range(1, n):
        if n % i == 0:
            result.append(i)
    return result

def d(n):
    return sum(divisors_of_n(n))

def main():
    result = []
    for i in range(1, 10000):
        if d(d(i)) == i and d(i) != i:
            result.append(i)
    return sum(result)

if __name__ == '__main__':
    start_time = time.time()
    main()
    print('Time taken: {} seconds'.format(time.time() - start_time))