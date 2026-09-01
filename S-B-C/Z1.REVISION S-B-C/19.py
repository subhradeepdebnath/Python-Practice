def counting(s):
    a=""
    for ch in s:
        if ch==" ":
            continue
        if ch in a:
            continue
        count=0
        for i in s:
                if ch==i:
                    count+=1
        print(ch, count)
        a=a+ch
s=input()
counting(s)