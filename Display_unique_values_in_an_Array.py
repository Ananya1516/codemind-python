n=int(input())
d=list(map(int,input().split()))
u_c=0
for i in range(n):
    count=0
    for j in range(n):
        if i!=j and d[i]==d[j]:
            count+=1
    if count==0:
        print(d[i],end=' ')
        u_c+=1
if u_c==0:
    print(-1)
        