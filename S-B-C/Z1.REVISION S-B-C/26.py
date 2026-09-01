def func(arr):
    for i in range(len(arr)):
        max=i
        for j in range(i+1,len(arr)):
            if arr[j]>arr[max]:
                max=j
        arr[i],arr[max]=arr[max],arr[i]
    print(*arr)
arr=list(map(int, input().split()))
func(arr)