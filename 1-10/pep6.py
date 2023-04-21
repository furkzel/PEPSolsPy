import time

def main():
    print((int(100*(1/2))*101) ** 2 - sum([i**2 for i in range(101)]))

if __name__ == "__main__":
    start = time.time()
    print(main())
    print(time.time() - start)
