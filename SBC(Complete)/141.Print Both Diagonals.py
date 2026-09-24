def func(matrix):
    left=[]
    right=[]
    for i in range(len(matrix)):
        left.append(matrix[i][i])
        right.append(matrix[i][n-1-i])
    print(left)
    print(right)
n=int(input())
matrix=[]
for i in range(n):
    matrix.append(list(map(int, input().split())))
func(matrix)