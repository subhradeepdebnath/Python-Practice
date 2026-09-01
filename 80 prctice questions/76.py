#  given a list of numbers, find the element with the highest frequency?
arr = [1, 2, 2, 3, 1, 4, 2]
max=0
answer=0
for i in arr:
    count=0
    for j in arr:
        if i==j:
            count+=1
    if count>max:
        max=count
        answer=i
print(answer)