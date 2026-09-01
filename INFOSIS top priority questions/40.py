arr=list(map(int, input().split()))
large=arr[0]
for i in arr:
    if i>large:
        large=i
print(large)
    