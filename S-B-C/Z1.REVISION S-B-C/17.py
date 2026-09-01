def coun(s):
    u=0
    l=0
    su=0
    n=0
    for ch in s:
        if ch.isupper():
            u+=1
        elif ch.islower():
            l+=1
        elif ch.isdigit():
            n+=1
        else:
            su+=1
    print (u,l,n,su )
s=input()
coun(s)