# Count the Number of Digits in a Given Number?
n=int(input())
count=0
while n>0:
    n=n//10
    count+=1
print(count)