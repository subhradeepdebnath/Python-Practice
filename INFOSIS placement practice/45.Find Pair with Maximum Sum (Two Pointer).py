# Find Pair with Maximum Sum (Two Pointer)
n=int(input())
arr=list(map(int, input().split()))
arr.sort()
for i in range(n):
    total=arr[n-2]+arr[n-1]
print(total)