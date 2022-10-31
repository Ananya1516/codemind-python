def getpf(num):
    s=0
    for i in range(1,num):
        if num%i==0:
            s=s+i
    return s
a=int(input())
b=int(input())
if getpf(a)==b and getpf(b)==a:
    print("Amicable")
else:
    print("Not Amicable")