import time
import os

def main():
    
    with open('11-20/pep18/number_triangle.txt', 'r') as f:
        lines = f.read().splitlines()
    
    lines = [i.split(' ') for i in lines]
    lines = [[int(j) for j in i] for i in lines]
    
    for i in reversed(range(len(lines)-1)):
        for j in range(len(lines[i])):
            lines[i][j] += max(lines[i+1][j], lines[i+1][j+1])

    print(lines[0][0])


if __name__ == '__main__':
    start_time = time.time()
    main()
    print('Time taken: {} seconds'.format(time.time() - start_time))