# Given a list of numbers, find the number of odd numbers.

arr=[1,3,2,44,23,442,31]
count=0
for i in arr:
    if i%2 !=0:
        count+=1
print(count)