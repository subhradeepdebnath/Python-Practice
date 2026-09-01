#  given numbers from 1 to N, one number is missing. Find the missing number?
n=int(input())
arr=list(map(int,input().split()))
sum=0
total=n*(n+1) // 2
for num in arr:
    sum+=num
missing=total-sum
print(missing)