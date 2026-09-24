def func(matrix):
    for i in range(n):
        for j in range(m):
            if matrix[i][j]!=matrix[j][i]:  # compare with transpose position
                print("Not Symmetric")
                return
    print("Symmetric")

n=int(input())
m=int(input())
matrix=[]
for i in range(n):
    matrix.append(list(map(int,input().split())))
func(matrix)