def func(s):
    a=""
    for i in range(len(s)-1,-1,-1):
        a=a+s[i]
    print(a)
s=input()
func(s)