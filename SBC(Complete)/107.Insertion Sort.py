def func(arr):
    for i in range(1, len(arr)):
        value=arr[i]
        j=i-1
        while j>=0 and arr[j]>value:
            arr[j+1] =arr[j]
            j-=1
        arr[j+1]=value
    print(*arr)
arr=list(map(int, input().split()))
func(arr)
