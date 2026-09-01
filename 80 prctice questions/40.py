#  given a string, count how many lowercase letters are present?
str = "HeLLo WoRLD"
count=0
for i in str:
    if i.islower():
        count+=1
print(count)