s=input()
for i in range(len(s)):
    count=0
    for j in range(len(s)):
        if s[i]==s[j]:
            count+=1
    if count==1:
        print(s[i])
        break