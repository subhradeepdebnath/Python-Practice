#  Given a number, count how many digits it contains.
n= int(input())
count=0
while n!=0:
    count+=1
    n=n//10
print(count)