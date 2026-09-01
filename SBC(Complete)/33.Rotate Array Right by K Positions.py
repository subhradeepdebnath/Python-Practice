def func(arr,k):
    for i in range(k):
        last=arr[-1]
        for j in range(len(arr)-1, 0, -1):
            arr[j]= arr[j-1]
        arr[0] = last
    print(*arr)
arr=list(map(int, input().split()))
k=int(input())
func(arr,k)