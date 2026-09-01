# Maximum Subarray Sum (Kadane's Algorithm)
n=int(input())
arr=list(map(int, input().split()))
maximum=arr[0]
current=arr[0]
for i in range(1,n):
    current=max(arr[i],current+arr[i])
    maximum=max(maximum,current)
print(maximum)