arr1=list(map(int, input().split()))
arr2=list(map(int, input().split()))
a=[]
for i in range(len(arr1)):
    if arr1[i] not in a:
        a.append(arr1[i])
for i in range(len(arr2)):
    if arr2[i] not in a:
        a.append(arr2[i])
a.sort()
print(*a)