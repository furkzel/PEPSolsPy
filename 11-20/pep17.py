import time

def number_letter_count(n):
    number_letter_counts = {'0':0, '1':3, '2':3, '3':5, '4':4, '5':4, '6':3, '7':5, '8':5, '9':4, '10':3, '11':6, '12':6, '13':8, '14':8, '15':7, '16':7, '17':9, '18':8, '19':8, '20':6, '30':6, '40':5, '50':5, '60':5, '70':7, '80':6, '90':6, '100':7, 'and':3, '1000':11}

    if str(n) in number_letter_counts:
        return number_letter_counts.get(str(n))
    elif str(n % 100) in number_letter_counts:
        return number_letter_counts.get(str(n//100)) + number_letter_counts.get(str(100)) + number_letter_counts.get('and') + number_letter_counts.get(str(((n % 100)//10)*10)) + number_letter_counts.get(str(n % 10))
    else:
        if n < 100:
            return number_letter_counts.get(str(n // 10 * 10)) + number_letter_counts.get(str((n % 10)))
        else:
            return number_letter_counts.get(str(n // 100)) + number_letter_counts.get(str(100)) + number_letter_counts.get('and') + number_letter_counts.get(str((n % 100) // 10 * 10)) + number_letter_counts.get(str((n % 10)))

def main():
    result = 0

    for i in range(1, 1001):
        result += number_letter_count(i)

    return result

if __name__ == "__main__":
    start = time.time()
    print(main())
    print(time.time() - start)