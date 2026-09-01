#  given an integer n, find the factorial of the number.
n=int(input())
num=1
for i in range(1,n+1):
    num=num*i
print(num)