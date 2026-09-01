#  Given an m × n matrix, find the smallest element present in the matrix.
row, col= map(int, input().split())
matrix=[]
for i in range(row):
    data=list(map(int, input().split()))
    matrix.append(data)
small=matrix[0][0]
for i in matrix:
    for j in i:
        if j<small:
            small=j
print(small)