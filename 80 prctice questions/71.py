# given a list of numbers, find the missing number from 1 to N?
arr = [1, 2, 4, 5]
for i in range(1, max(arr)+1):
    if i not in arr:
        print(i)