def func(n):
    temp=n
    total=0
    s=len(str(n))
    while temp>0:
        digit=temp%10
        total+=digit**s
        temp=temp//10
    if total==n:
        print("yes")
    else:
        print("NO")
n=int(input())
func(n)