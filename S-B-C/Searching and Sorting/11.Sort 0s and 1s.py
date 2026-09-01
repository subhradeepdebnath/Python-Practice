arr=list(map(int, input().split()))
a=[]
for i in range(len(arr)):
    if arr[i]==0:
        a.append(arr[i])
for i in range(len(arr)):
    if arr[i]==1:
        a.append(arr[i])
print(*a)