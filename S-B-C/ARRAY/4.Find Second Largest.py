arr=list(map(int, input().split()))
max=arr[0]
second=arr[0]
for i in range(len (arr)):
    if arr[i]>max:
        max=arr[i]
for i in range(len (arr)):
    if arr[i]<max and arr[i]>second:
        second=arr[i]
print(second)