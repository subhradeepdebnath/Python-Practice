def func(n):
    for i in range(2,n):
        if n%i==0:
            print("not prime")
            return
    else:
        print("prime")
n=int(input())
func(n)