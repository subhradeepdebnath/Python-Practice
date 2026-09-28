def func(arr):
    even=0
    odd=0
    for i in range(len(arr)):
        if arr[i]%2==0:
            even+=1
        else:
            odd+=1
    print(even)
    print(odd)
arr=list(map(int, input().split()))
func(arr)