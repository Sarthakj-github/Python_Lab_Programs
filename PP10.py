def selection_sort(L):
    n=len(L)
    for i in range(n-1):
        min=i
        for j in range(i+1,n):
            if L[min]>L[j]:
                min=j
        L[i],L[min]=L[min],L[i]
    return L

L=eval(input("Enter a list of numbers:"))

print("Unsorted List:-")
print(L)

Sorted_L=selection_sort(L)
print("Sorted List:-")
print(Sorted_L)

"""
Enter a list of numbers:[3,4,5,6,1,2,8,9,3,4]
Unsorted List:-
[3, 4, 5, 6, 1, 2, 8, 9, 3, 4]
Sorted List:-
[1, 2, 3, 3, 4, 4, 5, 6, 8, 9]
"""
