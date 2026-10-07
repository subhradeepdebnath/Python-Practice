def func(n,m,v):
    sum=0
    for i in range(n):
        p=m[i]*v[i]
        sum+=p
    print(sum)
n=int(input())
m,v=[],[]
for i in range(n):
    a,b=map(int, input().split())
    m.append(a)
    v.append(b)
func(n,m,v)