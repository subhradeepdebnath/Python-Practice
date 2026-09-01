#  given a string, count the number of vowels and consonants in it?
s=input().lower()
vowels=0
consonants=0
for ch in s:
    if ch in "aeiou":
        vowels+=1
    elif ch.isalpha():
        consonants+=1
print(vowels)
print(consonants)