def choice_sort(A):
    for top in range(1,len(A)-1):
        for j in range(top+1,len(A)):
            if A[j]<A[top]:
                A[top], A[j] = A[j], A[top]
