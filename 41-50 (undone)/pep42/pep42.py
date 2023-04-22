def triangle_number_generator(nth):
    for i in range(1, nth+1):
        yield int((i*(i+1))/2)

letters_values = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}

def word_value(word):
    return sum([letters_values[letter] for letter in word])

def is_triangle_number(n):
    for i in triangle_number_generator(n**2):
        if n == i:
            return True
    return False

def main():
    with open('PEPSolsPy\pep42\p042_words.txt', 'r') as f:
        words = f.read().replace('"', '').split(',')
    triangle_words = []
    for word in words:
        if is_triangle_number(word_value(word)):
            triangle_words.append(word)
    print(len(triangle_words))

if __name__ == '__main__':
    main()