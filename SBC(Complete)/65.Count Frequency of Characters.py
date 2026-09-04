def func(s):
    v=[]
    for ch in s:
        if ch not in v:
            count=0
            for i in s:
                if i==ch:
                    count+=1
            print(ch, count)
            v.append(ch)
s=input()
func(s)