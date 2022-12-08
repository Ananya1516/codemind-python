n=int(input())
d=list(map(int,input().split()))
e_s=o_s=0
for i in range(n):
    if i%2==0:
        e_s+=d[i]
    else:
        o_s+=d[i]
a_d=e_s-o_s
if a_d==0:
    print("YES")
else:
    print('NO')