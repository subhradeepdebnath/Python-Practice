#  given a decimal number, convert it to binary?
n=int(input())
binary=""
while n !=0:
    rem=n%2
    binary+=str(rem)
    num= n // 2
    n=num
print(binary[::-1])