# Left Rotate an Array by K Positions
n=int(input())
arr=list(map(int, input().split()))
key=int(input())
key=key%n
arr=arr[key:]+arr[:key]
print(*arr)