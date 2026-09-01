def dup(arr):
    a=[]
    for i in range(len(arr)):
        if arr[i] not in a:
            a.append(arr[i])
    print(a)
arr=list(map(int, input().split()))
dup(arr)