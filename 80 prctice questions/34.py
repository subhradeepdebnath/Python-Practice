#  given a string , count how many consonants are present?
str = "Hello World"
count=0
for i in str:
    if i not in "aeiou":
        count+=1
print(count)