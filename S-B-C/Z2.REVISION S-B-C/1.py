def func(arr):
    min=arr[0]
    max=arr[0]
    for i in range(len(arr)):
        if arr[i]<min:
            min=arr[i]
    for j in range(len(arr)):
        if arr[j]>max:
            max=arr[j]
    print("min:", min)
    print("max:", max)
arr=list(map(int, input().split()))
func(arr)