def func(s):
    a=""
    for ch in s:
        if ch not in a:
            a=a+ch
    print(a)
s=input()
func(s)