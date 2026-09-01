def func(arr):
    curr=arr[0]
    mini=arr[0]
    for i in range(1,len(arr)):
        curr=min(arr[i],curr+arr[i])
        if curr<mini:
            mini=curr
    print(mini)
arr=list(map(int, input().split()))
func(arr)