s=input()
a=""
for i in range(len(s)):
    if s[i] not in a:
        a=a+s[i]
print(a)