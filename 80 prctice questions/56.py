#  given a list of numbers, find the first repeating element?
arr = [5, 3, 4, 3, 5, 6]
for i in arr:
    count=0
    for j in arr:
        if i==j:
            count+=1
    if count>1:
            print(i)
            break