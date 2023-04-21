import time
import os

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
values = {alphabet[i]: i+1 for i in range(len(alphabet))}

def main():
    with open('21-30/pep22/p022_names.txt', 'r') as f:
        names = f.read().split(',')
    
    names = [i.strip('"') for i in names]
    names.sort()

    result = 0
    for i in range(len(names)):
        result += (i+1) * sum([values[j] for j in names[i]])

    print(result)

if __name__ == '__main__':
    start_time = time.time()
    main()
    print('Time taken: {} seconds'.format(time.time() - start_time))