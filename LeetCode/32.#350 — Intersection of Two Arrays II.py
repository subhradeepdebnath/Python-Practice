def func(arr,ar):
    a=[]
    b=list(ar)
    for i in range(len(arr)):
        if arr[i] in b:
            a.append(arr[i])
            b.remove (arr[i])
    print(*a)
arr=list(map(int, input().split()))
ar=list(map(int, input().split()))
func(arr,ar)