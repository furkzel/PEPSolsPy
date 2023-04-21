import time

def collatz(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3*n + 1
    
def collatz_sequence(n):
    sequence = []

    count = 0
    while n != 1:
        sequence.append(n)
        count += 1
        n = collatz(n)
        if count > 1000:
            break
    
    sequence.append(1)
    return len(sequence)

def main():
    max_number = 0
    max_length = 0
    for i in range(1, 1000000):
        if collatz_sequence(i) > max_length:
            max_length = collatz_sequence(i)
            max_number = i
    return max_number

if __name__ == "__main__":
    start = time.time()
    print(main())
    print(time.time() - start)
