# given an m*n matrix, print all the elements row-wise in a single line.
row, col=map(int, input().split())
matrix=[]
for i in range(row):
    data=list(map(int, input().split()))
    matrix.append(data)
for j in matrix:
    for i in j:
        print(i, end=" ")