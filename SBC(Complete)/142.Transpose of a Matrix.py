def func(matrix):
    for i in range(m):
        for j in range(n):
            print(matrix[j][i])
        print()
n=int(input())
m=int(input())
matrix=[]
for i in range(n):
    matrix.append(list(map(int, input().split())))
func(matrix)