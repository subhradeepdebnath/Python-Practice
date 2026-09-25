def func(matrix):
    n=len(matrix)
    m=len(matrix[0])
    result=[]
    for j in range(m):
        result.append(matrix[0][j])
    for i in range(1,n):
        result.append(matrix[i][m-1])
    for j in range(m-2, -1,-1):
        result.append(matrix[n-1][j])
    for i in range(n-2,0,-1):
        result.append(matrix[i][0])
    print(*result)
n=int(input())
m=int(input())
matrix=[]
for i in range(n):
    matrix.append(list(map(int, input().split())))
func(matrix)