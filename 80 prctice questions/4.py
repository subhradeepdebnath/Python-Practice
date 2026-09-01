# given a list of numbers, find the smallest number without using min() function.
arr=[8,5,18,6,99,2,444,1,54,56]
num=arr[0]
for i in arr:
    if i<num:
        smallest=i
        num=i
print(smallest)