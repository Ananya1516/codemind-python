n=int(input())
sqr=n**2
digits=len(str(n))
last_dig=sqr%pow(10,digits)
if last_dig==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")