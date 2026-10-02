def func(s):
    a=""
    b=""
    s=s.lower()
    for i in range(len(s)):
        if s[i].isalnum():
            a=a+s[i]
    for j in range(len(a)-1,-1,-1):
        b=b+a[j]
    if a==b:
        print("true")
    else:
        print("false")
s=input()
func(s)