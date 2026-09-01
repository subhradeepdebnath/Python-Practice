# given a list of numbers, rotate the list one step to the right?
arr = [1, 2, 3, 4, 5]
last=arr[-1]
new=[last]
for i in range(len(arr)-1):
    new.append(arr[i])
print(new)