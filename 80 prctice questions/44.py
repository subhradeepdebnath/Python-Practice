#  given a string , remove all the vowels and print the remaining string?
str = "hello world"
new=""
for i in str:
    if i not in "aeiou":
        new=new+i
print(new)
        