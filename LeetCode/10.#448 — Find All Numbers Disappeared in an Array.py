def func(arr):
    a=[]
    n=len(arr)
    for i in range(1,n+1):
        if i not in arr:
            a.append(i)
    print(*a)
arr=list(map(int, input().split()))
func(arr)