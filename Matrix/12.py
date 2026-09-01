#  Given an N × N matrix, print all the secondary diagonal elements.
n=int(input())
matrix=[]
for i in range(n):
    data=list(map(int, input().split()))
    matrix.append(data)
value=[]
for i in range(n):
    value.append(matrix[i][n-1-i])
print(value, end=" ")