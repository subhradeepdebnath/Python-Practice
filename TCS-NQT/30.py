#  given a string, remove all spaces from it and print the new string.
s=input()
words=s.split()
new=" "
for ch in s:
    if ch != " ":
        new+=ch
print(new)