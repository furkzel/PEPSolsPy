import os 
import time 

def main():
    
    number = ""
    
    with open('pep8/number.txt', 'r') as f:
        numbers = f.read().splitlines() 
    
    for line in numbers:
        number += line

    def product_of_13_numbers(number):
        product = 1
        for i in range(13):
            product *= int(number[i])
        return product
    
    def largest_product(number):
        largest = 0
        for i in range(len(number) - 13):
            if product_of_13_numbers(number[i:]) > largest:
                largest = product_of_13_numbers(number[i:])
        return largest

    print(largest_product(number))
    

if __name__ == "__main__": 
    start = time.time()
    main()
    print(time.time() - start)