n=int(input())
list=list(map(int,input().split()))

for i in range(1,len(list)):
    if(list[i]==list[i-1]):
        print("YES")
        break
else:
    print("NO")
    