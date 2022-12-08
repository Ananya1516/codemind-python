n=int(input())
d=list(map(int,input().split()))
count=0
for i in range(n):
    for j in range(n):
        if i!=j and d[i]!=0 and d[j]!=0 and d[i]==d[j]:
            count=count+1
            d[i]=0
            d[j]=0
            break
print(count)