n=int(input())
arr=list(map(int, input().split()))
ans=[]
for i in range(n):
    found=-1
    for j in range(i+1,n):
        if arr[i]<arr[j]:
            found=arr[j]
            break
    ans.append(found)
print(*ans)
        