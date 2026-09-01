# Check whether a Number is an Armstrong Number

n = int(input())

ori = n
sum = 0
count = 0

# Count number of digits
while n > 0:
    count += 1
    n = n // 10

n = ori

# Calculate Armstrong sum
while n > 0:
    digit = n % 10
    sum += digit ** count
    n = n // 10

if sum == ori:
    print("armstrong number")
else:
    print("not armstrong number")