#  given an integer n, check whether it is a prime number or not?
n=int(input())
prime=True
for i in range(2,n):
    if n%i==0:
        prime=False
if prime:
    print("prime number")
else:
    print("not prime number")