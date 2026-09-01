#  given a list of numbers, find all pairs whose sum is equal to a given number?
# target=5
arr = [1, 2, 3, 4, 5]
target = 5
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i]+arr[j]==target:
            print(arr[i],arr[j])