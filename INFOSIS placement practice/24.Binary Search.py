# Given a sorted array of N integers and a key, print the index of the key?
n=int(input())
arr=list(map(int, input().split()))
key=int(input())
low=0
high=n-1
found=False
while low<=high:
    mid=(low+high)//2
    if arr[mid]==key:
        print(mid)
        found=True
        break
    elif key> arr[mid]:
        low=mid+1
    else:
        high=mid +1
if not found:
    print(-1)