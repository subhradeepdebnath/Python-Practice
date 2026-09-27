def func(arr):
    for i in range(len(arr)-1):
        if arr[i]+1!=arr[i+1]:
            print(arr[i]+1)
            return
arr=list(map(int, input().split()))
func(arr)