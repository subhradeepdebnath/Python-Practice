n=int(input())
arr=list(map(int, input().split()))
key=int(input())
found=False
index=-1
for i in range(n):
    if arr[i]==key:
        found=True
        index=i
if found:
    print(index)
else:
    print(-1)