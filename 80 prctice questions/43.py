# given a string , count how many special character is presrent(like @,#.%)
str = "ab@c#1$d"
count=0 
for i in str:
    if not i.isalnum():
        count+=1
print(count)