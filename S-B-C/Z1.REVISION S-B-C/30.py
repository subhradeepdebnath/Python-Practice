def func(arr):
    a=[]
    for i in range(len(arr)):
        if arr[i] not in a:
            a.append(arr[i])
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i]>a[j]:
                a[i],a[j]=a[j],a[i]
    print(*a)
arr=list(map(int, input().split()))
func(arr)