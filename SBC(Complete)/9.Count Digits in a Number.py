# Count Digits in a Number?

def func(n):
    count=0
    while n>0:
        digit=n%10
        count+=1
        n=n//10
    print(count)
n=int(input())
func(n)