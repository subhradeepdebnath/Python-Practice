def func(n,arr,k):
    for i in range(len(arr)):
        if arr[i]==k:
            if i==0:
                print(-1)
                return
            if i%2==0:
                i-=1
            else:
                i+=1
            if i<len(arr):
                print(arr[i])
            else:
                print(-1)
n=int(input())
arr=list(map(int, input().split()))
k=int(input())
func(n,arr,k)