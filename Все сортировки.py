#Сортировка слиянием
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


#Сортировка пузырьком
def bubble_sort(A):
    for i in range(1,len(A)):
        for j in range(len(A)-i):
            if A[j]>A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]


#Сортировка выбором
def selection_sort(A):
    for top in range(1,len(A)-1):
        for j in range(top+1,len(A)):
            if A[j]<A[top]:
                A[top], A[j] = A[j], A[top]


#Сортировка вставками
def Insert_sort(A):
    for i in range(1,len(A)):
        top=i
        while A[top]>A[top-1]:
            A[top],A[top-1] = A[top-1],A[top]
            top-=1


#Сортировка Тони Хоара (Быстрая)
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
 
