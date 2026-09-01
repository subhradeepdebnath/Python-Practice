# given an integer n, check whether it is an armstrong number or not?
n=int(input())
temp=n
sum=0
while n!=0:
    digit=n%10
    sum=sum+digit*digit*digit
    n=n//10
if temp==sum:
    print("armstrong number")
else:
    print("Not armstrong number")