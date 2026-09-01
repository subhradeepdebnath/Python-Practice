arr=list(map(int, input().split()))
first=arr[0]
second=arr[0]
for i in range(len(arr)):
    if arr[i]>first:
        first=arr[i]
for j in range(len(arr)):
    if arr[j]>second and arr[j]<first:
        second=arr[j]
print(second)