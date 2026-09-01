#  given two integers, a and b , find their gcd (greatest common divisor)?
a=int(input())
b=int(input())
while b!=0:
    temp=b
    b= a% b 
    a=temp
print(a)