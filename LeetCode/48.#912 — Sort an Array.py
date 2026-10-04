def func(arr):
    for i in range(len(arr)):
        small=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[small]:
                small=j
        temp=arr[i]
        arr[i]=arr[small]
        arr[small]=temp
    print(*arr)
arr=list(map(int, input().split()))
func(arr)