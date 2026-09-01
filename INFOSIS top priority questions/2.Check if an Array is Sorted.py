# Check if an Array is Sorted
n=int(input())
arr=list(map(int, input().split()))
found=True
for i in range(n-1):
    if arr[i]>arr[i+1]:
        found=False
if found:
    print("YES")
else:
    print("NO")
        