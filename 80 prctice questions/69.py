#  given a list of numbers, rotate the list one step to the left?
arr = [1, 2, 3, 4, 5]
first=arr[0]
new=[]
for i in range(1,len(arr)):
    new.append(arr[i])
new.append(first)
print(new)