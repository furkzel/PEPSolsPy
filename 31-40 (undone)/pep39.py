import time

def generator_of_right_triangle_triplet():
    I = []
    for a in range(1, 1000):
        for b in range(a, 1000):
            for c in range(b, 1000):
                if a + b + c <= 1000 and a**2 + b**2 == c**2:
                    I.append((a, b, c))
    return I

def main():
    I = []
    L = []
    counts = []
    for triplet in generator_of_right_triangle_triplet():
        I.append(triplet)
        L.append(sum(list(triplet)))
    for i in L:
        count = 0
        for k in L:
            if i == k:
                count += 1
        counts.append(count)
    print(L[counts.index(max(counts))])

if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(end - start)

# 840
# 34.907029151916504
