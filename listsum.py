def listsum(l1, n):
    if n==0:
        return 0
    return l1[n-1]+listsum(l1,n-1)
print(listsum([1,2,3],3))
