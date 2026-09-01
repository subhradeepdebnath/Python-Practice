#  given two integers a and b, find their LCM( least common multiple)?
a= int(input())
b=int(input())
x=a
y=b
while y!=0:
    temp= y
    y= x%y
    x=temp
lcm=(a*b)//x
print(lcm)