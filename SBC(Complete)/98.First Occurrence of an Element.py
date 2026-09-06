def func(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            print(i)
            return
arr=list(map(int, input().split()))
target=int(input())
func(arr,target)