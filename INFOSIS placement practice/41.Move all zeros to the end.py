# Move all zeros to the end
n=int(input())
arr=list(map(int, input().split()))
a=[]
b=[]
c=[]
for i in arr:
    if i !=0:
        a.append(i)
    if i ==0:
        b.append(i)
for i in a:
    c.append(i)
for i in b:
    c.append(i)
print(c)