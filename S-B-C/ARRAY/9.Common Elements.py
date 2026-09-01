arr1=list(map(int, input().split()))
arr2=list(map(int, input().split()))
a=[]
for i in range(len(arr1)):
    for j in range(len(arr2)):
        if arr1[i] == arr2[j]:
            if arr1[i] not in a:
                a.append(arr1[i])
print(*a)