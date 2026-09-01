def rev(arr):
    a=[]
    for i in range(len(arr)-1,-1,-1):
        a.append(arr[i])
    return a
arr=list(map(int, input().split()))
print(rev(arr))