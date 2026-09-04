def func(s):
    rev=[]
    for i in range(len(s)-1,-1,-1):
        rev.append(s[i])
    print(*rev)
s=input().split()
func(s)