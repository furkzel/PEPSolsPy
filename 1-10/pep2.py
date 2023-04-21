# We define a fibonacci function that return the nth fibonacci number using recursive fibonacci definition.

import time


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def main():
    count = 0
    i = 0

    while fibonacci(i) < 4000000:
        if fibonacci(i) % 2 == 0:
            count += fibonacci(i)
        i += 1

    print(count)


if __name__ == "__main__":
    start = time.time()
    main()
    print(time.time() - start)


# We choosed this solution because 4000000 is not a big number as we thinked before. Recursivity is safe and fast in this case.
