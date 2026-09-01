#  given two list of numbers, find the union of the two lists without duplicates?
arr1 = [1, 2, 3, 4]
arr2 = [3, 4, 5, 6]
new=[]
for i in arr1:
    if i not in new:
        new.append(i)
for i in arr2:
    if i not in new:
        new.append(i)
print(new)