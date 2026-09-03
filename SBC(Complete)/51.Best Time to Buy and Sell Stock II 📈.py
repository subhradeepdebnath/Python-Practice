def func(arr):
    profit=0
    for i in range(len(arr)-1):
        if arr[i+1] > arr[i]:
            profit+=arr[i+1] - arr[i]
    print(profit)
arr=list(map(int, input().split()))
func(arr)