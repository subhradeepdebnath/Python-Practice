def func(arr,target):
    for i in range(len(arr)-1,-1,-1):
        if arr[i]==target:
            print(i)
            return
arr=list(map(int, input().split()))
target=int(input())
func(arr,target)