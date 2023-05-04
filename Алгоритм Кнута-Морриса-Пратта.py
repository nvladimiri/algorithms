def prefix(s):
    A = [0]*len(s)
    for i in range(1,len(s)):
        p = A[i-1]
        while p > 0 and s[p] != s[i]:
            p = A[p-1]
        if s[p] == s[i]:
            p += 1
        A[i] = p
    return A

def kmp(sub,t):
    index = -1
    f = prefix(sub)
    k = 0
    for i in range(len(t)):
        while k > 0 and s[k] != t[i]:
            k = f[k-1]
        if s[k] == t[i]:
            k += 1
        if k == len(sub):
            index = i - len(sub) + 1
            break
    return index
