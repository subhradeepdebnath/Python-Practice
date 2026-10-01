def func(arr):
    arr.sort()
    n=len(arr)
    for i in range(1,n+1):
        if i not in arr:
            print(i)
            return
    print(n+1)
arr=list(map(int, input().split()))
func(arr)