def func(arr):
    sum=0
    for i in range(len(arr)):
        sum+=arr[i]
    maximum=max(arr)
    total=0
    for i in range(1, maximum+1):
        total+=i
    final=total-sum
    print(final)
arr=list(map(int, input().split()))
func(arr)

