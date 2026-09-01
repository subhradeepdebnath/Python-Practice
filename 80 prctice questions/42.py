#  given a string count how many digits are present in it?
str = "a1b2c3d4"
count=0
for i in str:
    if i.isdigit():
        count+=1
print(count)