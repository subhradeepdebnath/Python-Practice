def func(num):
    for i in range(2,(num)-1):
        if num%i==0:
            print("not prime")
            break
        else:
            print("prime")
            break
num=int(input())
func(num)