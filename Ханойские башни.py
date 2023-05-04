def hanoi(src,dst,tmp,n):
    if n==0:
        return
    hanoi(src,tmp,dst,n-1)
    print(src,dst)
    hanoi(tmp,dst,src,n-1)
hanoi(1,2,3,3)
