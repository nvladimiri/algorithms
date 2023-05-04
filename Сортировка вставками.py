def Insert_sort(A):
    for i in range(1,len(A)):
        top=i
        while A[top]>A[top-1]:
            A[top],A[top-1] = A[top-1],A[top]
            top-=1
