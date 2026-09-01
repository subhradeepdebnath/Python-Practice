n=int(input())
arr=list(map(int, input().split()))
even=0
odd=0
for i in arr:
    if i %2==0:
        even+=1
    else:
        odd+=1
print(even)
print(odd)