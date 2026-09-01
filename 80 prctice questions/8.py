# Given a list of numbers, find the first occurrence index of a given number.
arr=[1,3,2,44,23,442,31]
key=2
index=0
for i in arr:
    if i==key:
        print(index)
    index+=1