def func(arr):
    a=[]
    b=[]
    for i in range(len(arr)):
        if arr[i] ==0:
            a.append(arr[i])
        else:
            b.append(arr[i])
    for i in range(len(arr)):
        if arr[i]==0:
            b.append(arr[i])
    print(*b)
            
arr=list(map(int, input().split()))
func(arr)