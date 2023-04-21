import time

def main():
    count = 0
    for i in range(1,10**6):
        I = []
        for j in str(i):
            I.append(int(j)**5)
        if sum(I) == i:
            count += i
    print(count - 1)
    
if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)
