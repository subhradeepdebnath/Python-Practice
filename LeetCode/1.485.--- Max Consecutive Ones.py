def func(arr):
    count=0
    max=0
    for i in range(len(arr)):
        if arr[i]==1:
            count+=1
        else:
            count=0
        if count>max:
            max=count
    print(max)
arr=list(map(int, input().split()))
func(arr)