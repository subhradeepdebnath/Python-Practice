#  given a list of numbers, find whether there exists any pair whose differences is equal to a given number?
arr = [1, 5, 3, 7, 9]
target = 4
found=False
for i in arr:
    for j in arr:
        if i-j==target:
            found=True
if found:
    print("pair found")
else:
    print("pair not found")