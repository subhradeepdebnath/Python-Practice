#  given a list of numbers, find the smallest even numbers?
arr = [7, 12, 3, 18, 5, 2]
n=arr[0]
for i in arr:
    if i%2==0:
        if i<n:
            n=i
print(n)
        