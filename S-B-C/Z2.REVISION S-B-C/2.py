def func(arr):
    sec=arr[0]
    first=arr[0]
    for i in range(len(arr)):
        if arr[i]>first:
            sec=first
            first=arr[i]
        elif (arr[i]>sec or first==sec) and arr[i]<first:
            sec=arr[i]
    if first==sec:
        print(-1) 
    else:
        print(sec)
arr=list(map(int, input().split()))
func(arr)