def func(arr):
    water=0
    for i in range(len(arr)):
        left_max=arr[i]
        for j in range(i):
            if arr[j] > left_max:
                left_max=arr[j]
        right_max=arr[i]
        for j in range(i+1, len(arr)):
            if arr[j]> right_max:
                right_max=arr[j]
        if left_max< right_max:
            level=left_max
        else:
            level=right_max
        water += level-arr[i]
    print(water)
n=int(input())
arr=list(map(int, input().split()))
func(arr)