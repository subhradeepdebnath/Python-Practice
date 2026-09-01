def func(arr1,arr2):
    a=[]
    for i in range(len(arr2)):
        if arr2[i] in arr1:
            a.append(arr2[i])
    print(*a)
arr1=list(map(int, input().split()))
arr2=list(map(int, input().split()))
func(arr1,arr2)