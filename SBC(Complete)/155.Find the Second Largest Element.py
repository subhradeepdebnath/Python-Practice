def func(arr):
    first=arr[0]
    second=None
    for i in range(len(arr)):
        if arr[i]>first:
            second=first
            first=arr[i]
        elif arr[i] != first and (second is None or arr[i] > second):
            second = arr[i]
    if second is None:
        print(-1)
    else:
        print(second)
arr=list(map(int, input().split()))
func(arr)