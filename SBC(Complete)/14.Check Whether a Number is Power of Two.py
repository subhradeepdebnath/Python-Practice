def func(n):
    count=0
    while n>0:
        if n%2==1:
            count+=1
        n=n//2
    if count==1:
        print("power of 2")
    else:
        print("not")
n=int(input())
func(n)