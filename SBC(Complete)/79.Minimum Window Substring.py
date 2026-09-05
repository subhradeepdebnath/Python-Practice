def func(s,t):
    minimum=len(s)+1
    answer=""
    for i in range(len(s)):
        a=""
        for j in range(i,len(s)):
            a=a+s[j]
            ok =True
            for ch in t:
                if a.count(ch)<t.count(ch):
                    ok=False
                    break
            if ok:
                if len(a)<minimum:
                    minimum=len(a)
                    answer=a
                    break
    if answer=="":
        print("no window")
    else:
        print(answer)
s=input()
t=input()
func(s,t)