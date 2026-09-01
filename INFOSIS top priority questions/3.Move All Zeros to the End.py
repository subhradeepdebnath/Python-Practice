n=int(input())
arr=list(map(int, input().split()))
a=[]
for i in arr:
    if i != 0:
        a.append(i)
for i in arr:
    if i == 0:
        a.append(i)
print(a)