#  given an m*n matrix, find the largest element present in the matrix?
row, col=map(int, input().split())
matrix=[]
sum=0
for i in range(row):
    data= list(map(int, input().split()))
    matrix.append(data)
large=matrix[0][0]
for i in matrix:
    for j in i:
            if j > large:
                large= j
print(large)