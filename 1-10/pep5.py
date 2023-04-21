# We define a lcm function. We have to define also a gcd function.

import time

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def main():
    count = 1
    for i in range(1, 21):
        count = lcm(count, i)
    print(count)

if __name__ == "__main__":
    start = time.time()
    main()
    print(time.time() - start)
    