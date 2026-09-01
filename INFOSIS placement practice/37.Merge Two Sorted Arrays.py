# Merge Two Sorted Arrays

n = int(input())
arr1 = list(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))

arr=arr1+arr2
arr.sort()
print(arr)