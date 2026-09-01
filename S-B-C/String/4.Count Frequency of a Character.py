s=input()
ch=input()
count=0
for i in range(len(s)):
    if ch==s[i]:
        count+=1
print(count)