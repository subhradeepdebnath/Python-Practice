#  given a list of numbers, move all zeros to the end of the list?
arr = [1, 0, 2, 0, 3, 4]
new=[]
nw=[]
for i in arr:
    if i==0:
        new.append(i)
    else:
        nw.append(i)
result= nw+new
print(result)
        