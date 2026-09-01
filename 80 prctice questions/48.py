#   given a list of numbers, find the product of all even numbers?
arr = [2, 3, 4, 5, 6]
prod=1
for i in arr:
    if i%2==0:
        prod*=i
print(prod)