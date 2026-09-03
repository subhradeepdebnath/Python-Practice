def func(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i][1] > arr[j][1]:
                arr[i], arr[j] = arr[j],arr[i]
    count=1
    last_end=arr[0][1]
    for i in range(1, len(arr)):
        if arr[i][0] >= last_end:
            count+=1
            last_end=arr[i][1]
    print(count)
n=int(input())
arr=[]
for i in range(n):
    data=list(map(int, input().split()))
    arr.append(data)
func(arr)