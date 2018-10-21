a=[]
n=int(input())
for i in range(n):
    x=int(input())
    a.append(x)
min=a[0]
for i in a:
    if i<min:
       min=i
print(min)
