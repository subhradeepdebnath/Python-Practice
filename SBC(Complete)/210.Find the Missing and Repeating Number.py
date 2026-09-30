def func(arr):
    arr.sort()
    for i in range(len(arr)-1):
        if arr[i]==arr[i+1]:
            repeat=arr[i]
    for i in range(1, len(arr)+1):
        if i not in arr:
            missing = i
    print(missing)
    print(repeat)
arr=list(map(int, input().split()))
func(arr)