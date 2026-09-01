# count how many times a character appears in a string?
str= "banana"
ch= "a"
count=0
for i in str:
    if i==ch:
        count+=1
print(count)