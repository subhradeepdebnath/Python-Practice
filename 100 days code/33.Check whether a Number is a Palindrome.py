# Check whether a Number is a Palindrome?
n=int(input())
rev=0
ori=n
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
if rev==ori:
    print("palindrome")
else:
    print("not palindrome")