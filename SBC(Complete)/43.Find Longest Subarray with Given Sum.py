def func(arr,target):
    maximum=0
    for i in range(len(arr)):
        sum=0
        for j in range(i,len(arr)):
            sum+=arr[j]
            if sum==target:
                length=j-i+1

                if length>maximum:
                    maximum=length

    print(maximum)
arr=list(map(int, input().split()))
target=int(input())
func(arr,target)