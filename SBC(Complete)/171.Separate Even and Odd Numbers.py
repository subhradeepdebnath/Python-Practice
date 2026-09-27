def func(arr):
    a=[]
    b=[]
    for i in range(len(arr)):
        if arr[i]%2==0:
            a.append(arr[i])
        else:
            b.append(arr[i])
    print(a+b)
arr=list(map(int, input().split()))
func(arr)