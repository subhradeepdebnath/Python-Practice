# Given an array of N integer and a key, print the index of the key.
n=int(input())
arr=list(map(int, input().split()))
key=int(input())
found=False
for i in range(n):
    if arr[i]==key:
        found=True
        break
if found:
    print(i)
else:
    print(-1)