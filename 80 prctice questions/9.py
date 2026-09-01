# Given a string, count how many vowels are present.
str="Hello world"
count=0
str=str.lower()
for ch in str:
    if ch in "aeiou":
        count+=1

print(count)
    