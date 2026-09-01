#  given a number, check whether it is a perfect number or not?
n=int(input())
sum=0
for i in range(1,n):
        if n%i==0:
            div=i
            sum+=div
if n==sum:
    print(n, " is a perfect number")
else:
    print(n, " is not a perfect number")
    
    