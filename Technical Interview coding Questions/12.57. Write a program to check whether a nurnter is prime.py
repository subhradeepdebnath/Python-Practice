def func(n):
    count=0
    if n<=1:
        print("not prime")
        return
    for i in range(2,n):
        if n%i==0:
            count+=1
    if count>0:
        print("not prime")
        return
    print("Prime")
n=int(input())
func(n)