def func(arr):
    n=len(arr)+1
    total=n*(n+1)//2
    sum=0
    for i in range(len(arr)):
        sum+=arr[i]
    print(total-sum)
arr=list(map(int, input().split()))
func(arr)