import time
import os

with open('pep13/number.txt', 'r') as f:
    number = ""
    number += f.read().replace('\n', '')

def main():
    result = 0
    for i in range(0, len(number), 50):
        result += int(number[i:i+50])
    
    print(str(result)[:10])

if __name__ == "__main__":
    start = time.time()
    main()
    print(time.time() - start)