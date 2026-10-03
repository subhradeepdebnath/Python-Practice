def func(arr):
    while arr!=1:
        sum=0
        while arr>0:
            d=arr%10
            a=d**2
            arr=arr//10
            sum+=a
        num=sum
    print("true")
    
arr=int(input())
func(arr)