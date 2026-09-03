def func(arr):
    a=[]
    for i in range(len(arr)):
        if arr[i]==0:
            a.append(arr[i])
    for i in range(len(arr)):
        if arr[i]==1:
            a.append(arr[i])
    for i in range(len(arr)):
        if arr[i]==2:
            a.append(arr[i])
    print(*a)
arr=list(map(int, input().split()))
func(arr)    