#  given a list of numbers, find the element having the maximum frequency?
arr = [1, 2, 2, 3, 1, 4, 2]
printed=[]
max_count=0
answer=0
for i in arr:
    if i not in printed:
        count=0
        for j in arr:
            if i==j:
                count+=1
            if count> max_count:
                max_count=count
                answer=i
        printed.append(i)
print(answer)