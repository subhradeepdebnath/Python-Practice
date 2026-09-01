#  given an integer n, print the reverse of the number?
n=int(input())
rev=0
while n!=0:
    new= n%10
    rev=rev*10+new
    n=n//10
print(rev)