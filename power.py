
def power2(n):
    if n==0:
        return 1
    return 2*power2(n-1)
op=power2(5)
print(op)