# Find Sum of Digits?
def func(n):
    sum=0
    while n>0:
        digit=n%10
        sum+=digit
        n=n//10
    print(sum)
n=int(input())
func(n)