# Check Whether a Number is Armstrong?

def func(n):
    a=[]
    num=n
    m=len(str(n))
    sum=0
    while n>0:
        digit=n%10
        sum+=digit**m
        n=n//10
    if num==sum:
        print("armstrong number")
    else:
        print("not an armstrong number")
n=int(input())
func(n)