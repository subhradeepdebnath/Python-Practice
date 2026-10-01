def func(arr):
    max=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[j]-arr[i]>max:
                max=arr[j]-arr[i]
    print(max)
arr=list(map(int, input().split()))
func(arr)