def func(s):
    u=0
    l=0
    d=0
    sp=0
    for ch in s:
        if ch.isupper():
            u+=1
        elif ch.islower():
            l+=1
        elif ch.isdigit():
            d+=1
        else:
            sp+=1
    print(u)
    print(l)
    print(d)
    print(sp)
s=input()
func(s)