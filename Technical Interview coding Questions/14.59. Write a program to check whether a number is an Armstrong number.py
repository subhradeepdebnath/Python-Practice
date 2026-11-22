def func(n):
    m=len(str(n))
    count=0
    for i in str(n):
        a=int(i)**m
        count+=a
    if n==count:
        print("armstrong number")
    else:
        print("not armstrong")
n=int(input())
func(n)