def insertion_sort(L):
    n=len(L)
    
    for i in range(1,n):
        key=L[i]
        j=i-1
        while j>=0 and L[j]>key:
            L[j+1]=L[j]
            j-=1
        L[j+1]=key
    return L

L=eval(input("Enter list of numbers:"))
print("Unsorted List:-")
print(L)

Sorted_L=insertion_sort(L)
print("Sorted List:-")
print(Sorted_L)

"""
Enter list of numbers:[1,3,7,2,4,6,9,8]
Unsorted List:-
[1, 3, 7, 2, 4, 6, 9, 8]
Sorted List:-
[1, 2, 3, 4, 6, 7, 8, 9]
"""
