n=int(input())
arr=list(map(int,input().split()))
x=int(input())

low=0
high=n-1

while low<=high:
    mid=(low+high)//2

    if arr[mid]==x:
        print(mid)
        break
    elif arr[mid]<x:
        low=mid+1
    else:
        high=mid-1
else:
    print(-1)