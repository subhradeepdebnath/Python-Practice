#  given a string, count how many uppercase letters are present?
str = "HeLLo WoRLD"
count=0
for i in str:
    if i.isupper():
        count+=1
print(count)