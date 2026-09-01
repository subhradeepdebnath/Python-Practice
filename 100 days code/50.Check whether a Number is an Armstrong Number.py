# Check whether a Number is an Armstrong Number?
n=int(input())
count=0
ori=n
sum=0

temp=n
while temp>0:
    count+=1
    temp=temp//10
while n>0:
    digit=n%10
    sum+=digit ** count
    n=n//10
if sum==ori:
    print("armstrong")
else:
    print("not armstrong")