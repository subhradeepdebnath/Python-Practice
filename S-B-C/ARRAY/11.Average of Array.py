arr=list(map(int, input().split()))
length=len(arr)
total=0
for i in range(len(arr)):
    total+=arr[i]
avg=total/length
print(avg)