def func(arr,target):
    left=0
    right=len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            print(mid)
            return
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    print("not found")
arr=list(map(int, input().split()))
target=int(input())
func(arr,target)
