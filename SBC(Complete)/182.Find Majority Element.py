def func(arr):
    length=len(arr)
    total=length//2
    for i in range(len(arr)):
        count=0
        for j in range(len(arr)):
            if arr[i]==arr[j]:
                count+=1
        if count>total:
            print(arr[i])
            return
    print(-1)
arr=list(map(int, input().split()))
func(arr)