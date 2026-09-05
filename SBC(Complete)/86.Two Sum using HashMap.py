def func(arr,target):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==target:
                print(arr[i],arr[j])
arr=list(map(int, input().split()))
target=int(input())
func(arr,target)