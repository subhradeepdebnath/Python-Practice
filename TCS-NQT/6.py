#  given an integer n, check whether it is a palindrome number or not?
n=int(input())
temp=n
rev=0
while n!=0:
    digit = n%10
    rev=rev*10+digit
    n=n//10
if temp==rev:
    print("palindrome")
else:
    print("not palindrome")