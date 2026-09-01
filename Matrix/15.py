# Given an m × n matrix, print the maximum element of every row.
row,col=map(int, input().split())
matrix=[]
for i in range(row):
    data=list(map(int, input().split()))
    matrix.append(data)
for i in matrix:
    large=i[0]
    for j in i:
        if j>large:
            large=j
    print(large)