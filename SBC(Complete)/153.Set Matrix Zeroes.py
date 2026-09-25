def func(matrix):
    zero_rows=[]  # store rows containing zero
    zero_cols=[]  # store columns containing zero

    for i in range(n):  # go through each row
        for j in range(m):  # go through each column
            if matrix[i][j]==0:  # check for zero
                zero_rows.append(i)  # store row index
                zero_cols.append(j)  # store column index

    for i in zero_rows:  # go through rows containing zero
        for j in range(m):  # go through all columns
            matrix[i][j]=0  # make entire row zero

    for j in zero_cols:  # go through columns containing zero
        for i in range(n):  # go through all rows
            matrix[i][j]=0  # make entire column zero

    for row in matrix:  # print each row
        print(*row)

n=int(input())
m=int(input())
matrix=[]
for i in range(n):
    matrix.append(list(map(int,input().split())))
func(matrix)