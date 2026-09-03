def func(arr):
    max=arr[0]
    for i in range(len(arr)):
        if arr[i]>max:
            max=arr[i]
    print(max)
arr=list(map(int, input().split()))
func(arr)
                
