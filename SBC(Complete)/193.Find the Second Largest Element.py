def func(arr):
    f=arr[0]
    s=None
    for i in range(len(arr)):
            if arr[i]>f:
                s=f
                f=arr[i]
            elif arr[i]!=f and (s is None or arr[i]>s):
                s=arr[i]
    if s is None:
        print(-1)
    else:
        print(s)
            
arr=list(map(int, input().split()))
func(arr)