#  given a list of numbers, find the element with the second highest frequency?
arr = [1, 2, 2, 3, 1,4, 4, 2]
max_fre=0
sec_fre=0
max=0
second=0
for i in arr:
    count=0
    for j in arr:
        if i==j:
            count+=1
    if count>max_fre:
        sec_fre=max_fre
        second=max
        
        max_fre=count
        max=i
    elif count>sec_fre and count<max_fre:
        sec_fre=count
        second=i
print(second)
        