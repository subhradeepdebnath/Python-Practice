# Check whether three sides can form a Valid Triangle?
n=int(input())
m=int(input())
o=int(input())
if m+n>o and m+o>n and n+o>m:
    print("valid triangle")
else:
    print("non-valid triangle")
    