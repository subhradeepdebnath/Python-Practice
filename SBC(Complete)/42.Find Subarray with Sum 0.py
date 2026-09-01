def func(arr):
    for i in range(len(arr)):
        sum=0
        for j in range(i,len(arr)):
            sum+=arr[j]
            if sum==0:
                for k in range(i,j+1):
                    print(arr[k], end=" ")
                return
arr=list(map(int, input().split()))
func(arr)