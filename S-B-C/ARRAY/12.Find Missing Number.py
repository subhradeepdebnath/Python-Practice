arr=list(map(int, input().split()))
arr.sort()
for i in range(len(arr)-1):
    if arr[i+1] != arr[i]+1:
        print(arr[i]+1)
        break