def sq_root(a):
    if a<0:
        return -1
    x=a
    for i in range(a):
        x=(x+a/x)/2
    return x

n=int(input("Enter a number:"))
ans=sq_root(n)
if ans<0:
    print("Square root is imaginary.")
else:
    print(f"Square root of {n} by Newton's method is:",round(ans,5))

"""
Enter a number:44435
Square root of 44435 by Newton's method is: 210.79611
"""
