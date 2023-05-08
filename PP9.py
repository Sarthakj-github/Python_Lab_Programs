def binary_search(L,k,f,l):
    if f<=l:
        m=(f+l)//2
        if L[m]==k:
            return m
        elif L[m]<k:
            return binary_search(L,k,m+1,l)
        else:
            return binary_search(L,k,f,m-1)
    return -1

L=eval(input("Enter a list:"))
key=int(input("Enter item to be searched:"))
n=len(L)
check=binary_search(L,key,0,n-1)
if check==-1:
    print(f"Key {key} is not found in the list.")
else:
    print(f"Key {key} is found on index {check} in the list.")

'''
Enter a list:[1,2,3,4,5,6,7,8]
Enter item to be searched:8
Key 8 is found on index 6 in the list.
'''

