def func(s):
    num=0
    sign=1
    for ch in s:
        if ch =="-":
            sign=-1
        elif ch.isdigit():
            num=num*10+int(ch)
        else:
            break
    print(num*sign)
s=input()
func(s)