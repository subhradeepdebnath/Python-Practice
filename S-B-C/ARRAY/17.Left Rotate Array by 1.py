arr=list(map(int, input().split()))
first=arr[0]
a=[]
for i in range(len(arr)):
    if arr[i] != first:
        if arr[i] not in a:
            a.append(arr[i])
for j in range(len(arr)):
    if arr[j] == first:
        a.append(arr[j])
print(*a)