def func(r,m):
    m=list(m)
    for i in range(len(r)):
        if r[i]  not in m:
            print("false")
            return
        m.remove(r[i])
    print("true")
r=input()
m=input()
func(r,m)