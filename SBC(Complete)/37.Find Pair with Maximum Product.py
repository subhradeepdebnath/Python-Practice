def func(arr):
    arr.sort()
    a=[]
    b=[]
    for i in range(len(arr)-1,-1,-1):
        a.append(arr[i])
    b.append(a[0])
    b.append(a[1])
    print(*b)
arr=list(map(int, input().split()))
func(arr)
