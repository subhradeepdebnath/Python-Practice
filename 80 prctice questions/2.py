# count how many even numbers are there in a list?
arr=[1, 22, 5, 66 , 45, 58, 4, 69, 7,5]
count=0
for i in arr:
    if i%2==0:
        num=i
        count= count +1
print(count)