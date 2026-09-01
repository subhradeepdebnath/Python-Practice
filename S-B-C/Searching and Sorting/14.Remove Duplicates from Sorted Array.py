arr=list(map(int,input().split()))
a=[]
for i in range(len(arr)):
    if arr[i] not in a:
        a.append(arr[i])
print(*a)