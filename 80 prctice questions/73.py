#  given a list of numbers, find the smallest element that appears only once?
arr = [4, 2, 7, 2, 9, 7, 5]
smallest=float('inf')
for i in arr:
    count=0
    for j in arr:
        if i==j:
            count+=1
    if count==1 and i<smallest:
            smallest= i
print(smallest)