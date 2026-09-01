#  given a list of numbers, find the frequency of each element?
arr = [1, 2, 2, 3, 1, 4, 2]
printed=[]
for i in arr:
    if i not in printed:
        count=0
        for j in arr:
            if i==j:
                count+=1
        print(i,"->", count)
        printed.append(i)