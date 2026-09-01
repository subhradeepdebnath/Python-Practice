# Given an array of integers arr and an integer target, return the indices of the two numbers such that they add up to the target.You may assume that exactly one solution exists.Return the indices, not the values.
n=int(input())
arr=list(map(int, input().split()))
target=70
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i]+arr[j]==target:
            print(i,j)
            break