def func(arr,k):
    arr.sort()
    i=0
    j=len(arr)-1
    sum=0
    while i<j:
        sum=arr[i]+arr[j]
        if sum==k:
            print(arr[i],arr[j])
            return
        elif sum>k:
            j-=1
        elif sum<k:
            i+=1
            
    print(-1)
arr=list(map(int, input().split()))
k=int(input())
func(arr,k)