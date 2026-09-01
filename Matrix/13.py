#  Given an N × N matrix, print only the upper triangular elements.
n=int(input())
matrix=[]
for i in range(n):
    data=list(map(int, input().split()))
    matrix.append(data)
for i in range(n):
    for j in range(n):
        if j>=i:
            print(matrix[i][j], end=" ")
    print()