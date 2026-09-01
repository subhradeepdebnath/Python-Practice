def func(arr):
    m=len(arr)
    n=m//2
    visited=[]
    for i in range(len(arr)):
        if arr[i] in visited:
            continue
        count=0
        for j in range(len(arr)):
            if arr[i]==arr[j]:
                count+=1
        if count>n:
            print(arr[i])
            visited.append(arr[i])
arr=list(map(int, input().split()))
func(arr)