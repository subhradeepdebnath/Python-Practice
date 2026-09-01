def func(arr):
    a=[]
    for i in range(len(arr)):
        if arr[i] != 0:
            a.append(arr[i])
    for j in range(len(arr)):
        if arr[j]==0:
            a.append(arr[j])
    print(a)
arr=list(map(int, input().split()))
func(arr)