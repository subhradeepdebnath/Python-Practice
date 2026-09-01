#  given an integer n, print the first n terms of fibonacci series?
n= int(input())
a=0
b=1
for i in range(n):
    print(a, end=" ")
    c=a+b
    a=b
    b=c