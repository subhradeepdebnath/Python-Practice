#  given a list of numbers, remove all the duplicate elements and print the new list?
arr = [1, 2, 2, 3, 4, 4, 5]
new=[]
for i in arr:
    if i not in new:
        new.append(i)
print(new)