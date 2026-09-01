#  given a list of numbers, find the count of elements that appear exactly once?
arr = [2, 3, 4, 2, 3, 5, 6]
count=0
for i in arr:
    start=0
    for j in arr:
        if i==j:
            start+=1
    if start==1:
        num=i
        count+=1
print(count)