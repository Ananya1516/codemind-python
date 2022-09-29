N=int(input())
sum=0
while N:
    d=N%10
    sum=sum*10+d
    N=N//10
print(sum)