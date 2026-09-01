# Find the Sum of all Even Numbers from 1 to N?
n=int(input())
sum=0
for i in range(1,n+1):
    if i%2==0:
        sum+=i
print(sum)