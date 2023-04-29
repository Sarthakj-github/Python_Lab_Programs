def merge_sort(L,l,r):
    if l<r:
        m=(l+r)//2
        merge_sort(L,l,m)
        merge_sort(L,m+1,r)
        merge(L,l,m,r)
    return L
        
def merge(L,l,m,r):
    M=[]
    i,j=l,m+1
    while i<=m and j<=r:
        if L[i]>L[j]:
            M.append(L[j])
            j+=1
        else:
            M.append(L[i])
            i+=1
    while i<=m:
        M.append(L[i])
        i+=1
    while j<=r:
        M.append(L[j])
        j+=1
    for i in range(l,r+1):
        L[i]=M[i-l]

L=eval(input("Enter list of numbers:"))
print("Unsorted List:-")
print(L)

Sorted_L=merge_sort(L,0,len(L)-1)
print("Sorted List:-")
print(Sorted_L)

"""
Enter list of numbers:[2,4,3,6,5,1,3,8,9,0,3]
Unsorted List:-
[2, 4, 3, 6, 5, 1, 3, 8, 9, 0, 3]
Sorted List:-
[0, 1, 2, 3, 3, 3, 4, 5, 6, 8, 9]
"""
