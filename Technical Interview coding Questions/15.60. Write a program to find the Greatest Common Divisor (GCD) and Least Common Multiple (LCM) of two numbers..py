def func(a,b):
    aa=[]
    bb=[]
    cc=[]
    mini=min(a,b)
    for i in range(1,mini+1):
        if a%i==0:
            aa.append(i)
    for j in range(1,mini+1):
        if b%j==0:
            bb.append(j)
    aa.sort()
    bb.sort()
    for i in aa:
        if i in bb:
            cc.append(i)
    print(cc[-1])
    print((a*b)//cc[-1])
a,b=map(int,input().split())
func(a,b)