arr=list(map(int, input().split()))
arr.sort()
sum=0
for j in range(1,len(arr)):
    sum=sum+arr[j]
print(sum)

        