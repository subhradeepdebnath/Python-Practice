#   given a matrix, find it transpose?
r = int(input())
c = int(input())

a = []

for i in range(r):
    row = list(map(int, input().split()))
    a.append(row)

for j in range(c):
    for i in range(r):
        print(a[i][j], end=" ")
    print()