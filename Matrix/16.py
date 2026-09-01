# Given an m*n matrix, print the minimum element of every column.
row , col= map(int, input().split())
matrix=[]
for i in range(row):
    data=list(map(int, input().split()))
    matrix.append(data)
for j in range(col):           
    small = matrix[0][j]      
    for i in range(row):      
        if matrix[i][j] < small:
            small = matrix[i][j]
    print(small)