import itertools

def reciprocal_cycle_len(n):
	seen = {}
	x = 1
	for i in itertools.count():
		if x in seen:
			return i - seen[x]
		else:
			seen[x] = i
			x = x * 10 % n
			
def main():
    max = 0
    for i in range(2,1000):
        if reciprocal_cycle_len(i) > max:
            max = i
    print(max)

if __name__ == "__main__":    
    main()
