# given the list of numbers, find the sum of all even numbers.
arr = [1, 2, 3, 4, 5, 6]
total=0
for i in arr:
    if i%2==0:
        total=total+i
print(total)