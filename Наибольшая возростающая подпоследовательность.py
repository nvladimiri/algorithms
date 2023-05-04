def gis(A):
    F=[0]*len(A)
    for i in range(len(A)):
        for j in range(i):
            if A[i]>A[j] and F[j]>F[i]:
                F[i]=F[j]
        F[i]+=1
    return F

def ir_gis(A):
    F = gis(A)
    i = len(A)
    Gis=[]
    last=max(F)
    i=F.index(last)
    Gis=[A[i]]
    while F[i]!=1:
        j=i-1
        while F[j]!=F[i]-1 or A[j]>=A[i]:
            j-=1
        i=j
        Gis.append(A[i])  
    return Gis[::-1]



print(gis([5,6,4,87,1,7,2,7,4,8,9,5,3,2,7,2,736,26,26,265]))
print(ir_gis([5,6,4,87,1,7,2,7,4,8,9,5,3,2,7,2,736,26,26,265]))
