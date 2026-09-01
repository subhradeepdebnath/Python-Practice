s=input()
max=0
ans=""
for i in range(len(s)):
    count=0
    for j in range(len(s)):
        if s[i]==s[j]:
            count+=1
    if count>max:
        max=count
        ans=s[i]
print(ans)