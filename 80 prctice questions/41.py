#  given a string , replace all spaces with hypen. 
str = "I love python"
new=""
for i in str:
    if i==" ":
        new= new+ "-"
    else:
        new = new +i
print(new)