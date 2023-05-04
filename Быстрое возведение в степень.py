def power(a,n):
    if n==1:
        return a
    if n%2==0:
        return power(a**2,n//2)
    return a*power(a,n-1)
