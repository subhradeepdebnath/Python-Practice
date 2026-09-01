def func(n):
    sum=0
    ori=n
    for i in range(1,n):
        if n%i==0:
            sum+=i
    if sum==ori:
        print("perfect number")
    else:
        print("not a perfect number")
n=int(input())
func(n)