def func(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                print("not sorted")
                return
    else:
        print("sorted")
arr=list(map(int, input().split()))
func(arr)