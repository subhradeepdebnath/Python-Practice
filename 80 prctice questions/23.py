#  given a list of numbers, find the smallest number without using min() function?
arr = [8, 5, 18, 6, 99, 2, 44]
count=arr[0]
for i in arr:
    if i<count:
        count=i
print(count)