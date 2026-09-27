def func(n):
    ori=n
    l=len(str(n))
    sum=0
    while n>0:
        digit=n%10
        sum=sum+digit ** l
        n=n//10
    if sum==ori:
        print("armstrong")
    else:
        print("not")
n=int(input())
func(n)