n=int(input())
sum=0
list=list(map(int,input().split()))
for i in range(1,len(list)-1):
    if list[i]>list[i-1]  and list[i]>list[i+1]:
        sum+=1
print(sum)