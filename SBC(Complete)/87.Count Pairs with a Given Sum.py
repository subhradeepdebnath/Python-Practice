def func(arr,target):
    count=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==target:
                count+=1
    print(count)
arr=list(map(int, input().split()))
target=int(input())
func(arr,target)