def value(a,b,c,d):
    small=a
    if(b<small):
        small=b
    elif c<small:
        small=c
    elif d<small:
        small=d
    return small
a,b,c,d=map(int,input().split())
print(value(a,b,c,d))
