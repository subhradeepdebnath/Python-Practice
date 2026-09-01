#  given a string , count how many times a particular character appears in the string?
str="banana"
ch="a"
count=0
for i in str:
    if i==ch:
        count+=1
print(count)