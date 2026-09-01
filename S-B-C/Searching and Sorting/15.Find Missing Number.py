arr=list(map(int, input().split()))
n=len(arr)+1
total=0
for i in range(1, n+1):
    total+=i
sum=0
for i in range(len(arr)):
    sum+=arr[i]
print(total-sum)