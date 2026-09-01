s=input()
vowel=0
consonant=0
for i in range(len(s)):
    if s[i]=="a" or s[i]=="e" or s[i]=="i" or s[i]=="o" or s[i]=="u":
        vowel+=1
    else:
        consonant+=1
print(vowel)
print(consonant)