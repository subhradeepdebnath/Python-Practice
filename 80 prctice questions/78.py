# given a list of number, find the first element whose frequency is exactly 1?
arr = [2, 3, 4, 2, 3, 5, 6]
for i in arr:
    count=0
    for j in arr:
        if i==j:
            count+=1
    if count==1:
        print(i)
        break