def func(arr):
    first=arr[0]
    sec=arr[0]
    for i in range(len(arr)):
        if arr[i]>first:
                first=arr[i]
    for j in range(len(arr)):
        if arr[j]>sec and arr[j]<first:
            sec= arr[j]
    print(sec)
arr=list(map(int, input().split()))
func(arr)