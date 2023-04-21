import time 

def main():

    def sieve_of_Eratosthenes(n):
        primes =  [True for i in range(n+1)] #we create a list of boolean values
        result_primes = []
        p = 2 #initial value of p
        while (p * p <= n):
            if (primes[p] == True):
                for i in range(p * 2, n+1, p):
                    primes[i] = False
            p += 1

        for p in range(2, n+1):
            if primes[p]:
                result_primes.append(p)

        return result_primes

    print(sum(sieve_of_Eratosthenes(2000000)))

if __name__ == "__main__":
    start = time.time()
    main()
    print(time.time() - start)
