# check whether a number is palindrome or not?
str= "madam"
emp=""
for i in str:
    emp= i+emp
print(emp)
if str== emp:
    print("string is palindrome")
else:
    print("string is not palindrome")
    