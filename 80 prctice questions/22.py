# given a list of numbers, find the largest number without using max() function?
arr = [5, 8, 12, 3, 7]
count= arr[0]
for i in arr:
    if i> count:
        count= i
print(count)
