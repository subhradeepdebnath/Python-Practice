def func(s):
    a=""
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            b=s[i:j]
            if b==b[::-1]:
                if len(b)>len(a):
                    a=b
    print(a)
s=input()
func(s)