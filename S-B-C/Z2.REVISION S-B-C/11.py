def func(n):
    mul=1
    if n<0:
        print(1)
    else:
        for i in range(1,n+1):
            mul*=i
        print(mul)
n=int(input())
func(n)