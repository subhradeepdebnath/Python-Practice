def func(s,m):
    a=sorted(s)
    b=sorted(m)
    if a==b:
        print("anagram")
    else:
        print("not")
s=input()
m=input()
func(s,m)