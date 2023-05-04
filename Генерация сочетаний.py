# C повторениями
def gen_combinations(n,m,prefix=None):
    prefix=prefix or []
    if m == 0:
        print(*prefix)
        return
    for i in range(1,n+1):
        prefix.append(i)
        gen_combinations(n,m-1,prefix)
        prefix.pop()
    return


#Без повторений
def gen_combinations_none(n,m,prefix=None):
    prefix=prefix or []
    if m == 0:
        print(*prefix)
        return
    for i in range(1,n+1):
        if i in prefix:
            continue
        prefix.append(i)
        gen_combinations_none(n,m-1,prefix)
        prefix.pop()
    return
 
