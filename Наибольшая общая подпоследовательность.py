def max_p(A,B):
    answer=""
    F=[[0]*(len(B)+1) for _ in range(len(A)+1) ]
    for i in range(1,len(A)+1):
        for j in range(1,len(B)+1):
            if A[i-1]==B[j-1]:
                F[i][j]=F[i-1][j-1]+1
            else:
                F[i][j]=max(F[i-1][j],F[i][j-1])
    return F
def _lcs_(A,B):
    F=max_p(A,B)
    LCS=[]
    i,j=len(A),len(B)
    while i>=0 and j>=0:
        if A[i-1]==B[j-1]:
            LCS.append(A[i-1])
            i-=1
            j-=1
        elif F[i-1][j]>F[i][j-1]:
            i-=1
        else:
            j-=1
    return LCS[::-1]

A=[1,6,3,7,2,8,58,3,8,3265,347,27,2,1,0,9,8,7,6,5,7,5,78,1]
B=[1,3,4,5,5,5,5,6,6,7,58,347,1,0,9,8,7,6,6,5,5,5,78,78,65,2]
print(_lcs_(A,B))
