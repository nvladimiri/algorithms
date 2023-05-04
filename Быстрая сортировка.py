def quick_sort(A):
    if len(A)<=1:
        return
    L=[]; M=[]; R=[];
    middle=A[0]
    for x in A:
        if x<middle:
            L.append(x)
        elif x==middle:
            M.append(x)
        else:
            R.append(x)
    quick_sort(L); quick_sort(R)
    k=0
    for x in L+M+R:
        A[k]=x
        k+=1
