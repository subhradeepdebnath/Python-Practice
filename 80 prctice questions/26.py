#  given a list of numbers, count how many numbers are even?
arr = [1, 2, 3, 4, 5, 6]
count=0
for i in arr:
    if i%2==0:
        count+=1
print (count)