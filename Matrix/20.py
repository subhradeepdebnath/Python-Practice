#  Given two matrices of the same size (m × n), print their difference.
row, col=map(int, input().split())
matrix1=[]
matrix2=[]
for i in range(row):
    data=list(map(int, input().split()))
    matrix1.append(data)
for i in range(row):
    data=list(map(int, input().split()))
    matrix2.append(data)
for i in range(row):
    for j in range(col):
        print(matrix1[i][j]-matrix2[i][j], end=" ")
    print()