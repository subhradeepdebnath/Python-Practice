#  given a string, count how many vowels are present?
str = "Hello World"
count=0
for i in str:
    if i in "aeiou":
        count+=1
print(count)