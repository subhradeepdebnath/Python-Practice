arr=list(map(int, input().split()))
target=int(input())
count=0
for i in range(len(arr)):
    if arr[i]==target:
        count+=1
print(count)
