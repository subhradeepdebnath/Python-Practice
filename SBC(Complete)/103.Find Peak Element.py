def func(arr):
    for i in range(len(arr)):
        if i==0:
            if arr[i]>arr[i+1]:
                print(arr[i])
                return 
        elif i==len(arr)-1:
            if arr[i]<arr[i-1]:
                print(arr[i])
                return
        else:
            if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
                print(arr[i])
                return
arr=list(map(int, input().split()))
func(arr)