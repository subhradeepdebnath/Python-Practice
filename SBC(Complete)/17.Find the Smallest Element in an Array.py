def func(arr):
    min=arr[0]
    for i in range(len(arr)):
        if arr[i]<min:
            min=arr[i]
    print(min)
arr=list(map(int, input().split()))
func(arr)