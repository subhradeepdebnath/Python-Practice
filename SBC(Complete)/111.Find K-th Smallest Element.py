def func(arr,k):
    arr.sort()
    print(arr[k-1])
arr=list(map(int,input().split()))
k=int(input())
func(arr,k)