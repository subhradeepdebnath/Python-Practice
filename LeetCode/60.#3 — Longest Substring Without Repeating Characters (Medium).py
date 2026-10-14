def func(s):
    a=""
    maxi=0
    for i in range(len(s)):
        for j in range(i,len(s)):
            if s[j] in a:
                break
            a=a+s[j]
            if len(a)>maxi:
                maxi=len(a)
        a=""
    print(maxi)
s=input()
func(s)