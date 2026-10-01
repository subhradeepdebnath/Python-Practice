def func(arr):
    n=len(arr)
    for i in range(len(arr)):
        left=0
        right=0
        for j in range(i):
            left=left+arr[j]
        for j in range(i+1, n):
            right=right+arr[j]
        if left== right:
            print(i)
            return
    print(-1)
arr=list(map(int, input().split()))
func(arr)