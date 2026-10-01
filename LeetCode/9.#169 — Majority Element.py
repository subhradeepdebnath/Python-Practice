def func(arr):
    n=len(arr)
    m=n/2
    for i in range(len(arr)):
        count=0
        for j in range(len(arr)):
            if arr[i]==arr[j]:
                count+=1
        if count>m:
            print(arr[i])
            return
arr=list(map(int, input().split()))
func(arr)