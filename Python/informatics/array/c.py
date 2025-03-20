n=int(input())
sum=0
list=list(map(int,input().split()))
for i in list:
    if(i>0):
        sum+=1
print(sum)