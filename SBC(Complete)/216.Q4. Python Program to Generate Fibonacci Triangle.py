def func(n):
    a=0
    b=1
    for i in range(n):
        for j in range(i+1):
            print(a,end=" ")
            c=a+b
            a=b
            b=c
        print()
n=int(input())
func(n)