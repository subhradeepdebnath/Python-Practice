def func(arr,key):
    count=0
    for i in range(len(arr)):
        if arr[i]==key:
            count+=1
    print(count)
arr=list(map(int, input().split()))
key=int(input())
func(arr,key)