def func(arr):
    count=0
    for i in range(len(arr)):
        sum=0
        for j in range(i,len(arr)):
            sum+=arr[j]

            if sum==0:
                length=j-i+1
                if length>count:
                    count=length
    print(count)
arr=list(map(int, input().split()))
func(arr)