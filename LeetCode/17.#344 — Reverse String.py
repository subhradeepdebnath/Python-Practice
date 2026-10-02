def func(s):
    a=[]
    for i in range(len(s)-1,-1,-1):
        a.append(s[i])
    print(*a, sep="")
s=input()
func(s)