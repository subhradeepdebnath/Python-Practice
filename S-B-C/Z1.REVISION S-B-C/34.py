def func(arr):
    a=[]
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i]==arr[j] and arr[i] not in a:
                a.append(arr[i])
    print(*a)
arr=list(map(int, input().split()))
func(arr)