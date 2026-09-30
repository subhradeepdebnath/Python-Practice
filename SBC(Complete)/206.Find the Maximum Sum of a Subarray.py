def func(arr):
    max=arr[0]
    for i in range(len(arr)):
        total=0
        for j in range(i,len(arr)):
            total+=arr[j]
            if total>max:
                max=total
    print(max)
            
arr=list(map(int, input().split()))
func(arr)