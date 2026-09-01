#  Given an N × N matrix, rotate it 90° clockwise and print the new matrix.
n= int(input())
matrix=[]
for i in range(n):
    data=list(map(int, input().split()))
    matrix.append(data)
for i in range(n):
    for j in range(n-1, -1, -1):
        print(matrix[j][i],end=" ")
    print()