n=int(input())
d=list(map(int,input().split()))
x=y=0
for i in range(n):
    if i%2==0:
        x+=d[i]
    else:
        y+=d[i]
a_d=x-y
if a_d%4==0:
    print("X")
else:
    print("Y")
        