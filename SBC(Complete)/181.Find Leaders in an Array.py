def func(arr):
    for i in range(len(arr)):
        l=True
        for j in range(i+1, len(arr)):
            if arr[i]<=arr[j]:
                l=False
                break
        if l:
            print(arr[i], end=" ")
arr=list(map(int, input().split()))
func(arr)