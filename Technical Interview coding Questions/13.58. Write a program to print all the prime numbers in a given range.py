def func(a,b):
    z=[]
    q=[]
    for i in range(a,b):
        count=0
        for j in range(2,i):
            if i%j==0:
                count+=1
        if i>1 and count==0:
            z.append(i)
    print(*z,sep=" ")
a,b=map(int,input().split())
func(a,b)