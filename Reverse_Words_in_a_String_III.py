n=input()
k=n.split()
l=[]
for i in k:
    l.append(i[::-1])
reverse=' '.join(l)
print(reverse)