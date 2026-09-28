def func(arr):
    sum=0
    l=len(arr)
    for i in range(len(arr)):
        sum+=arr[i]
    avg=sum/l
    print(avg)
arr=list(map(int, input().split()))
func(arr)