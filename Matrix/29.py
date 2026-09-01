#  Given an m × n matrix, print its elements in zig-zag (row-wise) order.
row, col=map(int, input().split())
matrix= []
for i in range(row):
    data=list(map(int, input().split()))
    matrix.append(data)
for i in range(row):

    if i % 2 == 0:
        for j in range(col):
            print(matrix[i][j],end=" ")

    else:
        for j in range(col - 1, -1, -1):
            print(matrix[i][j],end=" ")