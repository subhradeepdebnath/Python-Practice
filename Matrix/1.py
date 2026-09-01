# Take a matrix as input and print the matrix exactly as it was entered.
row, col= map(int, input().split())
matrix=[]
for i in range(row):
    data=list(map(int, input().split()))
    matrix.append(data)
for i in matrix:
    print(i)