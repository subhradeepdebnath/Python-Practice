def func(arr,k):
    count=0
    for i in range(len(arr)):
        sum=0
        for j in range(i,len(arr)):
            sum=sum+arr[j]
            if sum==k:
                count+=1
    print(count)
arr=list(map(int,input().split()))
k=int(input())
func(arr,k)