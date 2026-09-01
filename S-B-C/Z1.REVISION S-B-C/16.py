def cha(s):
    max=0
    ans=""
    for ch in s:
        count=0
        for j in s:
            if ch == j:
                    count+=1
        if count>max:
            max=count
            ans=ch
    print(ans)
s=input()
cha(s)