# find the largest character in a string alphabetically?
str= "elephant"
largest=str[0]
for i in str:
    if i>largest:
        largest= i
print(largest)