def func(arr):
    for i in range(len(arr)):
        count=0
        for j in range(len(arr)):
            if i!=j and arr[i]==arr[j]:
                count+=1
        if count==0:
            print(arr[i])
            return
arr=list(map(int, input().split()))
func(arr)