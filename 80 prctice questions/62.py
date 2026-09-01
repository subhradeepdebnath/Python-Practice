# given a list of numbers, count how many numbers are positive, negative and zero?
arr = [-2, 5, -1, 7, 0, -3, 4]
pos=0
neg=0
zero=0
for i in arr:
    if i>0:
        pos+=1
    elif i<0:
        neg+=1
    else:
        zero+=1
print("positive" , pos)
print("negative", neg)
print("zero:", zero)