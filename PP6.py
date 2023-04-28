def expo(a,b):
    return a**b

a=eval(input("Enter Base:"))
b=eval(input("Enter Power:"))

ans=expo(a,b)
print(f"{a}^{b} is {round(ans,5)}")

"""
Enter Base:12
Enter Power:8
12^8 is 429981696
"""
