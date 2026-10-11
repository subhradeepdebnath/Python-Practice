def func(arr):
    total=0
    for i in range(len(arr)):
        left=0
        right=0
        for j in range(i+1):
            if arr[j]>left:
                left=arr[j]
        for j in range(i,len(arr)):
            if arr[j]>right:
                right=arr[j]
        water=min(left,right)-arr[i]
        total=total+water
    print(total)
arr=list(map(int, input().split()))
func(arr)