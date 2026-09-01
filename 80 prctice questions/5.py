# given a list of numbers, count how many numbers are greater than 10.
arr=[4, 15, 8, 21, 3, 12]
num=10
count=0
for i in arr:
    if i>num:
        total=i
        count += 1
print(count)