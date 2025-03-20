n=int(input())
sum=0
list=list(map(int,input().split()))
for i in range(1,len(list)):
    if(list[i]>list[i-1]):
        sum+=1
print(sum)