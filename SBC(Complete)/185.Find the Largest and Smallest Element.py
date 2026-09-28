def func(arr):
    arr.sort()
    print(arr[0], arr[-1])
arr=list(map(int, input().split()))
func(arr)