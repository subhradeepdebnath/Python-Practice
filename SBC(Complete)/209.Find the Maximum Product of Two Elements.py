def func(arr):
    arr.sort()
    m=arr[-1]*arr[-2]
    n=arr[0]*arr[1]
    if m>n:
        print(m)
    else:
        print(n)
arr=list(map(int, input().split()))
func(arr)