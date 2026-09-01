def func(arr1,arr2):
    a=[]
    for i in range(len(arr1)):
        a.append(arr1[i])
    for j in range(len(arr2)):
        if arr2[j] not in a:
            a.append(arr2[j])
    a.sort()
    print(*a)
arr1=list(map(int, input().split()))
arr2=list(map(int, input().split()))
func(arr1,arr2)