import os 
import time

def product_of_4_numbers(L):
    up = []
    down = []
    left = []
    right = []
    diagonal = []

    for i in range(len(L)):
        for j in range(len(L[0])):
            if j <= len(L[0])-4:
                right.append(L[i][j]*L[i][j+1]*L[i][j+2]*L[i][j+3])
            if i <= len(L)-4:
                down.append(L[i][j]*L[i+1][j]*L[i+2][j]*L[i+3][j])
            if i <= len(L)-4 and j <= len(L[0])-4:
                diagonal.append(L[i][j]*L[i+1][j+1]*L[i+2][j+2]*L[i+3][j+3])
            if i <= len(L)-4 and j >= 3:
                diagonal.append(L[i][j]*L[i+1][j-1]*L[i+2][j-2]*L[i+3][j-3])

    print( max(up+down+left+right+diagonal) )


def main():
    with open('numbers.txt', 'r') as f:
        numbers = f.read().splitlines()

    nums = []

    for i in numbers:
        for k in range(0,len(i.replace(' ','')),2):
            nums.append(int(i.replace(' ','')[k:k+2]))

    nums_matrix = []

    for i in range(0,len(nums),20):
        nums_matrix.append(nums[i:i+20])

    nums_matrix
    
    product_of_4_numbers(nums_matrix)

if __name__ == "__main__": 
    start = time.time()
    main()
    print(time.time() - start)
