# Sum of Array Elements
n= int(input())
arr=list(map(int, input().split()))
sum=0
for i in arr:
    sum=sum+i
print(sum)