def func(arr):
    curr=arr[0]
    maxi=arr[0]
    for i in range(1,len(arr)):
        curr=max(arr[i], curr+arr[i])
        if curr>maxi:
            maxi=curr
    print(maxi)
arr=list(map(int, input().split()))
func(arr)