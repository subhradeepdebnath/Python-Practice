def func(arr,ar):
    a=[]
    for i in range(len(arr)):
        if arr[i] in ar:
            a.append(arr[i])
    print(*a)
arr=list(map(int, input().split()))
ar=list(map(int, input().split()))
func(arr,ar)