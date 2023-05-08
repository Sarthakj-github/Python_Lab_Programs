def linear_search(L,k):
    n=len(L)
    for i in range(n):
        if L[i]==k:
            return i
    return -1

L=eval(input("Enter a list:"))
key=eval(input("Enter item to be searched:"))

check=linear_search(L,key)
if check==-1:
    print(f"Key {key} not found in the list.") # see in edit mode.
else:
    print(f"Key {key} is found on index {check} in the list.")

'''
Enter a list:[1,2,34,5,6,2,8]
Enter item to be searched:8
Key 8 is found on index 6 in the list.
'''
