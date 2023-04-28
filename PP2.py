def Mul_Mat(A,B):
    m1,n1=len(A),len(A[0])
    m2,n2=len(B),len(B[0])
    M=[]
    if n1==m2:
        for i in range(m1):
            m=[]
            for j in range(n2):
                s=0
                for k in range(m2):
                    s+=A[i][k]*B[k][j]
                m.append(s)
            M.append(m)
    return M

A=eval(input("Enter Matrix A:"))
B=eval(input("Enter Matrix B:"))
if A==[] or B==[]:
    print("Empty matrix is not accepted.")
else:
    M=Mul_Mat(A,B)
    if M==[]:
        print("No.of columns in A is not equal to No. of rows in B.")
    else:
        m=len(M)
        n=len(M[0])
        print("Multiplication Matrix:-")
        for i in range(m):
            for j in range(n):
                print(M[i][j],end=' ')
            print()

"""
Enter Matrix A:[[3,4],[6,3],[8,2]]
Enter Matrix B:[[1,4,2],[5,4,3]]
Multiplication Matrix:-
23 28 18 
21 36 21 
18 40 22
"""
