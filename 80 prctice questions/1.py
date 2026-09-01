# Given a list of numbers, find the largest number without max() function.
arr = [ 5, 8 ,12, 3, 5, 7]
largest=arr[0]
for i in arr:
    if i> largest:
        largest= i
    
print(largest)