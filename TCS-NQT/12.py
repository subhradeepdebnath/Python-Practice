#  given a year, check whether it is a leap year or not?
n=int(input())
if n%4==0 and n%100!=0:
    print("leap year")
elif n%400==0:
    print("leap year")
else:
    print("not a leap year")