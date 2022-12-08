n=int(input())
d=list(map(int,input().split()))
for i in range(n):
    count=0
    for j in range(n):
        if i!=j and d[i]>d[j]:
            count+=1
    print(count,end=' ')