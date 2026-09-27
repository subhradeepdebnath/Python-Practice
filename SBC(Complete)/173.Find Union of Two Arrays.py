def func(arr,ar):
    a=[]
    for i in range(len(arr)):
        if arr[i]  not in a:
            a.append(arr[i])
    for j in range(len(ar)):
            if ar[j]  not in a:
                a.append(ar[j])
    print(*a)
arr=list(map(int, input().split()))
ar=list(map(int, input().split()))
func(arr,ar)