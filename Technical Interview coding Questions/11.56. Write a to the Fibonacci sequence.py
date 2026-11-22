def func(arr):
    a=0
    b=1
    for i in range(arr):
        print(a, end=" ")
        c=a+b
        a=b
        b=c
arr=int(input())
func(arr)