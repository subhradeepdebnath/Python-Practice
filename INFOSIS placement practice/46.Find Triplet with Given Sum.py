# Find Triplet with Given Sum
n=int(input())
arr=list(map(int,input().split()))
key=int(input())

arr.sort()

found=False

for i in range(n):
    left=i+1
    right=n-1

    while left<right:
        total=arr[i]+arr[left]+arr[right]

        if total==key:
            found=True
            break
        elif total<key:
            left+=1
        else:
            right-=1

    if found:
        break

if found:
    print("Triplet Found")
else:
    print("Not Found")