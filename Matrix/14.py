#  Given an m × n matrix, print only the boundary elements in clockwise order.
row,col=map(int, input().split())
matrix=[]
for i in range(row):
    data=list(map(int, input().split()))
    matrix.append(data)
for j in range(col):
    print(matrix[0][j], end=" ")
for i in range(1,row):
    print(matrix[i][col-1],end=" ")
for j in range(col-2,-1, -1):
    print(matrix[row-1][j], end=" ")
for i in range(row-2, 0, -1):
    print(matrix[i][0], end=" ")