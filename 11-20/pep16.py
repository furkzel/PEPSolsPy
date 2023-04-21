import time

def main():
    return sum([int(i) for i in str(2**1000)])

if __name__ == "__main__":
    start = time.time()
    print(main())
    print(time.time() - start)