import time

def fibonacci(nth):
    l = [1,1]
    for i in range(2,nth):
        l.append(l[i-1]+l[i-2])
    return l[nth-1]

def main():
    count = 200
    while len(str(fibonacci(count))) < 1000:
        count += 1
    print(count)

if __name__ == "__main__":
    start = time.time()
    main()
    print(time.time() - start)