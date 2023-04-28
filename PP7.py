def max_num(L):

    m=-float("inf")
    for i in L:
        if m<i:
            m=i
    return m

L=eval(input("Enter a list of numbers:"))
if L==[]:
    print("List is Empty.")
else:
    mx=max_num(L)
    print("Max number from the list is:",mx)

'''
Enter a list of numbers:[2,4,1,5,2,7,3,8,9]
Max number from the list is: 9
'''
