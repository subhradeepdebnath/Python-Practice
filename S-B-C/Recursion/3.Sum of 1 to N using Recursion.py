def func(n):
    sum=0
    if n==0:
        return 0
    else:
        return n+ func(n-1)
n=int(input())
print(func(n))