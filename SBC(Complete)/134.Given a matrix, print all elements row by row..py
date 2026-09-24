def func(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")
n=int(input())
matrix=[]
for i in range(n):
    matrix.append(list(map(int, input().split())))
func(matrix)