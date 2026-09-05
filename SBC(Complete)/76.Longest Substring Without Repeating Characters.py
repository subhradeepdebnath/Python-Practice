def func(s):
    maximum=0
    for i in range(len(s)):
        a=""
        for j in range(i,len(s)):
            if s[j] in a:
                break
            a=a+s[j]
            if len(a)> maximum:
                maximum=len(a)
    print(maximum)
s=input()
func(s)