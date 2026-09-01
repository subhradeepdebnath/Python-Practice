# Given a string, reverse it without using slicing ([::-1]).
str="Hello"
emp=" "
for i in str:
    emp=i + emp
print(emp)