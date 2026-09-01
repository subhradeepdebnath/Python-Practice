# Check Whether a Number is Prime?

def func(n):
    while n>1:
        for i in range(2,n):
            if n%i==0:
                print("Not prime")
                return
        else:
            print("prime")
            return
n=int(input())
func(n)