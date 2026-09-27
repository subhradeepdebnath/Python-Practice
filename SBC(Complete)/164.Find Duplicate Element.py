def func(arr):
    a=[]
    for i in range(len(arr)):
        if arr[i] not in a:
            a.append(arr[i])
        else:
            print(arr[i])
            break
arr=list(map(int, input().split()))
func(arr)