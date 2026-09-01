
n=int(input())
arr=list(map(int, input().split()))
m=[]
for i in arr:
    if i not in m:
        m.append(i)
print(m)