def func(arr):
    sum=0
    for i in range(len(arr)):
        sum+=arr[i]
    print(sum)
arr=list(map(int, input().split()))
func(arr)