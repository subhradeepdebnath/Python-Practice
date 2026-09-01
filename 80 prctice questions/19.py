# check whether a number is palindrome or not?
num=1231
original=num
rev=0
while num>0:
    nums= num%10
    rev=rev*10+nums
    num=num//10
print(rev)
if rev==original:
    print("palindrome")
else:
    print("not palindrome")