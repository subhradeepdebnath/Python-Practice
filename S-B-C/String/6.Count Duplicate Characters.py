s=input()
a=[]
for i in range(len(s)):
    if s[i] not in a:
        count=0
        for j in range(len(s)):
            if s[i]==s[j]:
                count+=1
        if count>=2:
            print(s[i], count)
        a.append(s[i])