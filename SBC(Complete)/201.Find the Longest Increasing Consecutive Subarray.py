def func(arr):
    count=1
    max=1
    for i in range(1, len(arr)):
        if arr[i]>arr[i-1]:
            count+=1
        else:
            count=1
        if count>max:
            max=count
    print(max)
arr=list(map(int, input().split()))
func(arr)