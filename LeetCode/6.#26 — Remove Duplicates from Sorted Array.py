def func(arr):
    a=[]
    n=len(arr)
    count=0
    for i in range(len(arr)):
        if arr[i] not in a:
            a.append(arr[i])
    m=len(a)
    print("k=",m)
    print(*a)
arr=list(map(int, input().split()))
func(arr)