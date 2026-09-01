#  given a list of number,separate all even and odd numbers into two different list?
arr = [1, 2, 3, 4, 5, 6]
even=[]
odd=[]
for i in arr:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("even=", even)
print("odd=", odd)