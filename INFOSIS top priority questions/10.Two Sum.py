# Two Sum
n=int(input())
arr=list(map(int, input().split()))
t=int(input())
found=False
for i in range(n):
    for j in range(i+1,n):
        if arr[i] +arr[j]==t:
            found=True
            break
if found:
    print("YES")
else:
    print("NO")