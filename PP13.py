def n_primes(n):
    primes=[2]
    num=3
    while len(primes)<n:
        prime=1
        for i in primes:
            if num%i==0:
                prime=0
                break
        if prime:
            primes.append(num)
        num+=2
    return primes

n=int(input("Enter number of primes:"))
primes=n_primes(n)
print(f"{n} prime numbers are:-")
for i in primes:
    print(i,end=' ')

"""
Enter number of primes:10
10 prime numbers are:-
2 3 5 7 11 13 17 19 23 29
"""
