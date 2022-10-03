n=int(input())
sum=0
x=n*n
while x:
    d=x%10
    sum=sum+d
    x=x//10
if sum==n:
    print("Neon Number")
else:
    print("Not Neon Number")
    