def func(arr):
    max=0
    sum=0
    for i in range(len(arr)):
        sum+=arr[i]
        if sum>max:
            max=sum
        if sum<0:
            sum=0
    print(max)
            
arr=list(map(int, input().split()))
func(arr)