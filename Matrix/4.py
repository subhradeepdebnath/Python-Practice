#  given an m *n matrix, print all the elements column by column.
row,col=map(int, input().split())
matrix=[]
for i in range(row):
        data=list(map(int,input().split()))
        matrix.append(data)
for i in range(col):
    for j in range(row):
        print(matrix[j][i])
    print()