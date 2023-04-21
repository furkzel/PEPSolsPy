def main():
    I = []
    for i in range(2, 101):
        for j in range(2, 101):
            I.append(i**j)
    I.sort()
    I = set(I)
    print(len(I))

main()