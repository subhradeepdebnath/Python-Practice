# find the products of digit of numbers?
num= 234
digit=1
while num>0:
    nums=num%10
    digit= digit * nums
    num=num//10
print(digit)