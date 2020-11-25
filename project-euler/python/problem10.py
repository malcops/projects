def sumPrimes(n):

    # sieve is list of size n, set to all True
    sum, sieve = 0, [True] * n
    for p in range(2, n):
        # if True, it is a prime
        if sieve[p]:
            sum += p
            # cross out every p number in the list
            for i in range(p*p, n, p):
                sieve[i] = False
    return sum

print(sumPrimes(2000000))

