n=int(input())
arr=list(map(int, input().split()))
diff=0
max=arr[0]
min=arr[0]
for i in range(n):
    if arr[i]>max:
        max=arr[i]
    if arr[i]<min:
        min=arr[i]
diff=max-min
print(diff)