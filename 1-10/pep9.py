import time 

def main():
    for a in range(1, 1000):
        for b in range(1, 1000):
            c = 1000 - a - b
            if a**2 + b**2 == c**2:
                return a*b*c
    
if __name__ == "__main__":
    start = time.time()
    print(main())
    print(time.time() - start)