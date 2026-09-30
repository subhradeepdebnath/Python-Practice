def func(arr):
    arr.sort()
    dif=arr[-1]-arr[0]
    print(dif)
arr=list(map(int, input().split()))
func(arr)