def even(arr):
    count=0
    for i in range(len(arr)):
        if arr[i]%2==0:
            count+=1
    return count
arr=list(map(int, input().split()))
print(even(arr))