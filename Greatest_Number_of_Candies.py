n=int(input())
d=list(map(int,input().split()))
e_c=int(input())
lst=[]
for i in range(n):# 2 3 5 1 3
     max=d[0]
for i in range(n):
     if d[i]>max:
          max=d[i]
for i in range(n):
     sum=e_c+d[i]
     if sum>=max:
         lst.append(True)
     else:
          lst.append(False)
print(*lst)
       


