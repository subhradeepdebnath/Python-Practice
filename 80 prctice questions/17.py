#  find the sum of digits of a number?
num=245
sum=0
while num >0:
    n=num % 10
    sum= sum + n
    num = num //10
print(sum)