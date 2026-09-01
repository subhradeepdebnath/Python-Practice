#  reverse a number?
num=245
rev=0
while num>0:
    nums= num%10
    rev=rev*10+nums
    num=num//10
print(rev)