def func(s):
    for ch in s:
        count=0
        for i in s:
            if ch==i:
                count+=1
        if count>1:
            print(ch)
            return
s=input()
func(s)