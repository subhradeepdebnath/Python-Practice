#  given a list of numbers, count how many numbers are odd?
arr = [1, 2, 3,7, 4, 5, 6]
count=0
for i in arr:
    if i%2!=0:
        count+=1
print (count)