# n чисел в m позициях
def generate_permutations(n:int, m:int, prefix=None):
    prefix=prefix or []
    if m==0:
        print(*prefix)
        return
    for elem in range(1,n+1):
        if elem in prefix:
            continue
        prefix.append(elem)
        generate_permutations(n,m-1,prefix)
        prefix.pop()
