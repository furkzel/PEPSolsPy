import time

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def main():
    return sum(int(i) for i in str(factorial(100)))

if __name__ == "__main__":
    start = time.time()
    print(main())
    print(time.time() - start)

