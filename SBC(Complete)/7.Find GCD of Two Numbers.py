# Find GCD of Two Numbers?

def func(a,b):
    while b!=0:
        rem=a%b
        a=b
        b=rem
    print(a)
a=int(input())
b=int(input())
func(a,b)