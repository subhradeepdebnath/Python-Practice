def func(arr):
    a=[]
    while arr>0:
        b=arr%2
        a.append(b)
        c= arr//2
        arr=c
    a.reverse()
    rev=0
    for i in a:
        rev=rev*10+i
    print(rev)
    
    
arr=int(input())
func(arr)