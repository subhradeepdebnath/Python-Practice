# Check whether a year is a Leap Year?
y=int(input())
if y%400==0:
    print("leap year")
elif y%4==0 and y%100!=0:
    print("leap year")
else:
    print("Not a leap year")