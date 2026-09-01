n=int(input())
arr=list(map(int, input().split()))
key=int(input())
count=0
for i in arr:
    if i == key:
        count+=1
print(count)