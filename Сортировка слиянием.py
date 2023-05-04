def  merge(A,B):
    C=[None]*(len(A)+len(B)
    k=i=j=0
    while i<len(A) and j<len(B):
        if A[i]<=B[j]:
            C[k]=A[i]
            k+=1
            i+=1
        else:
            C[k]=B[j]
            k+=1
            j+=1
    while i<len(A):
        C.append(A[i])
        i+=1
    while i<len(B):
        C.append(B[j])
        j+=1
    return C

def merge_sort(A):
    if len(A)<=1:
        return
    middle=len(A)//2
    L=A[:middle]
    R=A[middle:]
    merge_sort(L)
    merge_sort(R)
    C=merge(L,R)
    for i in range(len(A)):
        A[i]=C[i]
