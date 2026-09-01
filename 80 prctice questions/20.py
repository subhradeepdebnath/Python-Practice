# check whether a number is prime or not?
num=7
prime=True
for i in range(2, num):
    if num%i==0:
        prime= False
if prime:
    print("it is a prime number")
else:
    print("Not a prime number")