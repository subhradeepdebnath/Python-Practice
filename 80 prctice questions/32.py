#  given a list of numbers, find the 2nd largest number without using sort() and max().?
arr = [10, 5, 8, 20, 15]
largest=arr[0]
second=arr[0]
for i in arr:
    if i > largest:
        second=largest
        largest=i
    elif i>second and i!=largest:
        second=i
print(second)