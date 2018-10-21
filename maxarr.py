a=[]
n=int(input())
for i in range(n):
    x=int(input())
    a.append(x)
max=a[0]
for i in a:
    if i>max:
       max=i
print(max)
