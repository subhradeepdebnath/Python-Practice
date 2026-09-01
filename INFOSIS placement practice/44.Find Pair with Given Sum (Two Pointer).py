# Find Pair with Given Sum (Two Pointer)
n=int(input())
arr=list(map(int,input().split()))
key=int(input())
left=0
right=n-1
found=False
while left<right:
    total=arr[left]+arr[right]
    if total==key:
        found=True
        break
    elif total<key:
        left+=1
    else:
        right-=1
if found:
    print("Pair Found")
else:
    print("Not Found")