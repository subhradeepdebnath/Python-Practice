# given a list of numbers, find the average of all numbers?
list=[2, 4, 6, 8]
sum=0
for i in list:
    sum=sum + i 
    avg= sum/len(list)
print(avg)