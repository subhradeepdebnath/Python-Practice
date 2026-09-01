def sec(arr):
    first=arr[0]
    for i in range(len(arr)):
        if arr[i]>first:
            first=arr[i]
    second=None
    for j in range(len(arr)):
        if arr[j]<first:
            if second==None or arr[j]>second:
                second=arr[j]
    return second
arr=list(map(int, input().split()))
print(sec(arr))