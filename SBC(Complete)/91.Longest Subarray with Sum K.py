def func(arr,k):
    maximum=0
    for i in range(len(arr)):
        sum=0
        for j in range(i,len(arr)):
            sum=sum+arr[j]
            if sum==k:
                length=j-i+1
                if length>maximum:
                    maximum=length
    print(maximum)
arr=list(map(int,input().split()))
k=int(input())
func(arr,k)