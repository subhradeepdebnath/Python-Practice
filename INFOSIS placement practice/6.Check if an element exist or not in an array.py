n=int(input())
arr=list(map(int, input().split()))
key=int(input())
found=False
for i in arr:
    if i==key:
        found=True
if found:
    print("Found")
else:
    print("Not Found")