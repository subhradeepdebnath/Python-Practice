s=input()
letter=0
digit=0
special=0
for i in range(len(s)):
    if s[i].isalpha():
        letter+=1
    elif s[i].isdigit():
        digit+=1
    else:
        special+=1
print(letter)
print(digit)
print(special)