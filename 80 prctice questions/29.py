# given a list of numbers, find the largest even numbers?
arr = [3, 8, 11, 20, 5, 14]
num=0
for i in arr:
    if i%2==0:
        if(i>num):
            num=i
print(num)