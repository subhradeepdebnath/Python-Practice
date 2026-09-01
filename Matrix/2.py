# given an m * n matrix, print each row on a separate line.
row,col=map(int, input().split())
matrix=[]
for i in range(row):
    data=list(map(int, input().split()))
    matrix.append(data)
for i in matrix:
    print(*i)