import time

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def main():
    m = 21
    n = 21
    return factorial(m + n - 2) // (factorial(m - 1) * factorial(n - 1))

if __name__ == "__main__":
    start = time.time()
    print(main())
    print(time.time() - start)
    