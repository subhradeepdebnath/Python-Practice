def sum(arr):
    summ=0
    for i in range(len(arr)):
        summ+=arr[i]
    return summ
arr=list(map(int, input().split()))
print(sum(arr))