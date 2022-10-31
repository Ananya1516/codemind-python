a=int(input())
b=int(input())
pf_a=0
for i in range(1,a):
    if a%i==0:
        pf_a+=i
pf_b=0
for i in range(1,b):
    if b%i==0:
        pf_b+=i
if pf_a == b and pf_b == a:
    print("Amicable")
else:
    print("Not Amicable")
       