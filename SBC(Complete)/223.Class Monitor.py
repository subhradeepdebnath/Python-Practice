def func(arr):
    count=0
    for i in range(len(arr)):
            if arr[i]>arr[i-1]:
                count+=1
    print(count)
            
arr=list(map(int,input().split()))
func(arr)