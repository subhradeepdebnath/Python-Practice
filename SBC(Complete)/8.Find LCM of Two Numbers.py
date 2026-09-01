# Find LCM of Two Numbers?

def func(a,b):
    oria=a
    orib=b
    while b!=0:
        rem=a%b
        a=b
        b=rem
    m=a
    lcm=(oria*orib)/m
    print(lcm)
a=int(input())
b=int(input())
func(a,b)