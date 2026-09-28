def func(arr):
    small=arr[0]
    second=None
    for i in range(len(arr)):
            if arr[i]<small:
                second=small
                small = arr[i]
            elif arr[i]!=small and( second is None or arr[i]<second):
                second=arr[i]
    if second is None:
        print(-1)
    else:
        print(second)
arr=list(map(int, input().split()))
func(arr)