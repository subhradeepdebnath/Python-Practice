#  find the minimum element in array?
n=int(input())
arr=list(map(int, input().split()))
small=arr[0]
for i in arr:
    if i<small:
        small=i
print(small)
