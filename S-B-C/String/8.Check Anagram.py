s=input()
n=input()
if len(s)!= len(n):
    print("not anagram")
else:
    flag=True
    for i in range(len(s)):
        count1=0
        count2=0
        for j in range(len(s)):
            if s[i]==s[j]:
                count1+=1
            if s[i] == n[j]:
                count2+=1
        if count1!=count2:
            flag=False
            break
    if flag:
        print("anagram")
    else:
        print("not anagram")