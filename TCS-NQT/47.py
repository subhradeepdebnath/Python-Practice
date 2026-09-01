#  given a string and a character, remove all occurrences of that character from the string.
n=input()
m=input()
new=""
for i in n:
    if i!=m:
        new+=i
print(new)