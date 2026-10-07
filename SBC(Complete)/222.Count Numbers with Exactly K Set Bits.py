def func(n,k):
    total=0
    for i in range(1,n):
        count=0
        a=i

        while a>0:
            r=a%2
            if r==1:
                count+=1
            a=a//2
        if count==k:
            total+=1
    print(total)
n,k=map(int, input().split())
func(n,k)