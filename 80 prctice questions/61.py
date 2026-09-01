# given a list of numbers, create a new list containing only negative numbers?
arr = [-2, 5, -1, 7, 0, -3, 4]
new=[]
for i in arr:
    if i<0:
        new.append(i)
print(new)