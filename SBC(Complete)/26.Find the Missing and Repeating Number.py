def func(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i]==arr[j]:
                print("repeating number:", arr[i])
    for i in range(1, len(arr)+1):
        if i not in arr:
            print("missing number", i)
arr=list(map(int, input().split()))
func(arr)