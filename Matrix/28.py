#  Given an m × n matrix, print its elements in wave form.
row, col=map(int, input().split())
matrix= []
for i in range(row):
    data=list(map(int, input().split()))
    matrix.append(data)
for j in range(col):

    if j % 2 == 0:
        for i in range(row):
            print(matrix[i][j], end=" ")

    else:
        for i in range(row - 1, -1, -1):
            print(matrix[i][j], end=" ")