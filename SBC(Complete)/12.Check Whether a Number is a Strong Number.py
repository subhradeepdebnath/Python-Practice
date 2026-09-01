def func(n):
    ori=n
    total=0
    while n>0:
        digit=n%10
        prod=1
        for i in range(1,digit+1):
            prod*=i
        total+=prod
        n=n//10
    if total==ori:
        print("strong number")
    else:
        print("not a strong number")
n=int(input())
func(n)