import time

from itertools import permutations

def lexicographic_permutations():
    return ''.join(list(permutations('0123456789', 10))[999999])

if __name__ == '__main__':
    start = time.time()
    print(lexicographic_permutations())
    print(time.time() - start)
    