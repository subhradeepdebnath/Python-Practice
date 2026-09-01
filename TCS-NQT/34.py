# Given a string, check whether it is a palindrome or not.
s=input()
a=""
for ch in s:
    a = ch + a
if a==s:
    print("palindrome")
else:
    print("Not palindrome")