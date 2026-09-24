def func(matrix):
        sum=[]
        for i in range(len(matrix)):
            total=0
            for j in range(len(matrix[i])):
                total=total+matrix[i][j]
            sum.append(total)
        print(*sum)
n=int(input())
m=int(input())
matrix=[]
for i in range(n):
    matrix.append(list(map(int, input().split())))
func(matrix)