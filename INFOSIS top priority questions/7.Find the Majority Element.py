# Find the Majority Element
n=int(input())
arr=list(map(int, input().split()))
found=False
for i in arr:
    count=0
    for j in arr:
        if i==j:
            count+=1
    if count>n//2:
        print(i)
        found=True
        break
if not found:
    print(-1)