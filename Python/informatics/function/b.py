def power(x,n):
    res=1
    for _ in range(n):
        res*=x
    return res
x,n=map(float,input().split())
print(power(x,int(n)))