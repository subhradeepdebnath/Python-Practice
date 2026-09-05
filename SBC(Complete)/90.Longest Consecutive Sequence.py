def func(arr):
    arr.sort()
    count=1
    maximum=1
    for i in range(len(arr)-1):
        if arr[i+1]==arr[i]+1:
            count+=1
        else:
            count=1
        if count>maximum:
            maximum=count
    print(maximum)

arr=list(map(int,input().split()))
func(arr)