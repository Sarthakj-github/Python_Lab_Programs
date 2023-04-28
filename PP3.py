# GCD by recursion.
def gcd_r(a,b):
    if a==b:
        return a
    elif a>b:
        return gcd_r(a-b,b)
    else:
        return gcd_r(a,b-a)

# GCD by loop.
def gcd_l(a,b):
    while a!=b:
        if a>b:
            a-=b
        else:
            b-=a
    return a

# GCD by Euclidean Algorithm.
def gcd_ecl(a,b):
    if b==0:
        return a
    return gcd_ecl(b,a%b)

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))

gcd_r=gcd_r(a,b)
gcd_l=gcd_l(a,b)
gcd_ecl=gcd_ecl(a,b)

print(f"GCD of {a} and {b} by loop:",gcd_l)

print(f"GCD of {a} and {b} by recursion:",gcd_r)

print(f"GCD of {a} and {b} by Euclidean Algorithm:",gcd_ecl)

"""
Enter first number:210
Enter second number:120
GCD of 210 and 120 by loop: 30
GCD of 210 and 120 by recursion: 30
GCD of 210 and 120 by Euclidean Algorithm: 30
"""
