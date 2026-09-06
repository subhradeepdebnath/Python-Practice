def func(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            print(i)
            return
    print(-1)
arr=list(map(int,input().split()))
target=int(input())
func(arr,target)