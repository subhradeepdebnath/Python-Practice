#  given a list of numbers, find the difference between largest and the smallest numbers?
arr = [5, 2, 9, 1, 7]
largest=arr[0]
smallest=arr[0]
for i in arr:
    if i>largest:
        largest=i
    if i<smallest:
        smallest=i
dif=largest-smallest
print(dif)