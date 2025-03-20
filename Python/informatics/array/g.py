n=int(input())
sum=0

list=list(map(int,input().split()))
for i in range(len(list)//2):
    temp=list[i]
    list[i]=list[len(list)-i-1]
    list[len(list)-i-1]=temp
for i in list:
    print(i,end=" ")