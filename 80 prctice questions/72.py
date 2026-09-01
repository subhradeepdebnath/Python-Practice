#  given a list of numbers, find the largest element that appears only once?
arr = [4, 2, 7, 2, 9, 7, 5]
largest=0
for i in arr:
    count=0
    for j in arr:
        if j==i:
            count+=1
    if count==1 and i>largest:
        largest=i
print(largest)