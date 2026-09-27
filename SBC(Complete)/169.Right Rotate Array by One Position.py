def func(arr):
    a=arr[-1]
    b=[]
    for i in range(len(arr)-1):
        b.append(arr[i])
    print(*([a]+b))
arr=list(map(int, input().split()))
func(arr)