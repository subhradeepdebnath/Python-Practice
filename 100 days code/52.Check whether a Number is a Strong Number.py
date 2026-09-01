# Check whether a Number is a Strong Number?
n=int(input())
ori=n
sum=0
while n>0:
    digit=n%10
    n=n//10
    fac=1
    for i in range(1,digit+1):
        fac=fac*i
    sum=sum+fac
if sum==ori:
    print("strong number:")
else:
    print("not strong number")