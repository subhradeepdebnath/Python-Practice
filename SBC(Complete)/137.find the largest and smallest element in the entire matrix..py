def func(matrix):
    maximum=matrix[0][0]
    minimum=matrix[0][0]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j]>maximum:
                maximum=matrix[i][j]
            if matrix[i][j]<minimum:
                minimum=matrix[i][j]
    print(maximum)
    print(minimum)
n=int(input())
m=int(input())
matrix=[]
for i in range(n):
    matrix.append(list(map(int, input().split())))
func(matrix)