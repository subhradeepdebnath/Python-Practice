def func(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=func(arr[:mid])
    right=func(arr[mid:])
    result=[]
    i=0
    j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result=result+left[i:]
    result=result+right[j:]
    return result

arr=list(map(int,input().split()))
arr=func(arr)
print(*arr)