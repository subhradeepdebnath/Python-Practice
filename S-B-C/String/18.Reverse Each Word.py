s = input()
arr = s.split()
a = ""

for i in range(len(arr)):
    word = ""

    for j in range(len(arr[i])-1, -1, -1):
        word = word + arr[i][j]

    a = a + word + " "

print(a)