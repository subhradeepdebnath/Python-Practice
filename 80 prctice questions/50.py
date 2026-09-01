#  given a list of numbers , find the sum of all the prime numbers in the list?
arr = [2, 3, 4, 5, 6, 7, 8]
count=0
for num in arr:
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            count+=num
print(count)