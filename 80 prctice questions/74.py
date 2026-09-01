#  given a list of numbers, find the first element that appears exactly twice?
arr = [4, 2, 7, 2, 9, 7, 5]
for i in arr:
    count=0
    for j in arr:
        if i==j:
            count+=1
    if count==2:
        num=i
        break
print(num)