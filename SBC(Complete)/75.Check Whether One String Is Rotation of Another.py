def func(s,m):

    if len(s)!=len(m):
        print("Not Rotation")
        return

    a=s+s

    if m in a:
        print("Rotation")
    else:
        print("Not Rotation")

s=input()
m=input()

func(s,m)