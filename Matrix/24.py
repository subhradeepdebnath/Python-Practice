row, col = map(int, input().split())

matrix = []

for i in range(row):
    data = list(map(int, input().split()))
    matrix.append(data)

n = int(input())

found = False

for i in matrix:
    if n in i:
        found = True
        break

if found:
    print("Found")
else:
    print("Not Found")