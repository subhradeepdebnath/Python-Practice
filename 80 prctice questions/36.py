# given a string, check whether the string is palindrome or not?
word= "mam"
rev=""
for i in word:
    rev= i+rev
if rev==word:
    print("word is palindrome")
else:
    print("word is not palindrome")