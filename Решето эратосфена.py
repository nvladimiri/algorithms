n=int(input())
A=[True]*(n+1)
A[0]=A[1]=False
for i in range(2,n+1):
    if A[i]:
        for j in range(2*i,n+1,i):
            A[j]=False
for q in range(len(A)):
    if A[q]:
        print(q,end=" ")
