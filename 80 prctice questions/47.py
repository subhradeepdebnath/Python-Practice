#  given a list of numbers, count how many numbers are divisible by 3?
arr = [3, 5, 6, 9, 10, 12]
count=0
for i in arr:
    if i%3==0:
        count+=1
print(count)