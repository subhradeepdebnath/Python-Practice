def func(arr):
    count=0
    for j in range(len(arr)):
        if n==arr[j]:
            count+=1
    print(count)
arr=list(map(int, input().split()))
n=int(input())
func(arr)