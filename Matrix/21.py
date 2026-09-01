#  Given two matrices:
# Matrix A of size m × n
# Matrix B of size n × p
# Print their multiplication.

row, col= map(int, input().split())
matrix=[]
for i in range(row):
    data=list(map(int, input().split()))
    matrix.append(data)
row1, new= map(int, input().split())
matrix1=[]
for i in range(row1):
    data=list(map(int, input().split()))
    matrix1.append(data)
for i in range(row):
    for j in range(new):
        total=0
        for k in range(col):
            total=total+matrix[i][k]*matrix1[k][j]
        print(total, end=" ")
    print()