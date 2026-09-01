# heck whether a Number is a Perfect Number?
n=int(input())
ori=n
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i
if ori==sum:
    print("perfect number")
else:
    print("not perfect number")