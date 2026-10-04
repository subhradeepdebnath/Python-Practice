def func(arr):
    a=[]
    for i in range(len(arr)):
        a.append(arr[i]**2)
    a.sort()
    print(*a)
arr=list(map(int, input().split()))
func(arr)