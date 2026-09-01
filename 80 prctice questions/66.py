#  given a list of numbers, find the intersection of two list?
arr1 = [1, 2, 3, 4]
arr2 = [3, 4, 5, 6]
for i in range(len(arr1)):
    for j in range(len(arr2)):
        if arr1[i]==arr2[j]:
            print(arr1[i],arr2[j])