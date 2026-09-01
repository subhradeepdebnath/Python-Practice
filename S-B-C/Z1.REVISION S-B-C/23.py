def func(arr,key):
    low=0
    high=len(arr)-1
    ans=-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==key:
            ans=mid
            high =mid-1
        elif arr[mid]<=key:
            low=mid+1
        else:
            high=mid-1
    return ans
arr=list(map(int,input().split()))
key=int(input())
print(func(arr,key))