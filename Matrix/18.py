#  given an m*n matrix, print its transpose?
row , col= map(int, input().split())
matrix=[]
for i in range(row):
    data=list(map(int, input().split()))
    matrix.append(data)
for j in range(col):
    for i in range(row):
        print(matrix[i][j], end=" ")
    print()