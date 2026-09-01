def func(s,a):
    p=sorted(s)
    q=sorted(a)
    if p==q:
        print("yes")
    else:
        print("no")
s=input()
a=input()
func(s,a)