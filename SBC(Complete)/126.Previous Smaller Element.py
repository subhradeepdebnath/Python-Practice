def func(arr):
    a=[]
    for i in range(len(arr)):
        for j in range(i-1,-1,-1):
            if arr[j]<arr[i]:
                a.append(arr[j])
                break
        if len(a)==i:
            a.append(-1)
    print(*a)
arr=list(map(int, input().split()))
func(arr)