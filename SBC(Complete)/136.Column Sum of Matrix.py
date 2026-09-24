def func(matrix):
    total=[]
    for i in range(m):
        sum=0
        for j in range(n):
            sum+=matrix[j][i]
        total.append(sum)
    print(*total)
n=int(input())
m=int(input())
matrix=[]
for i in range(n):
    matrix.append(list(map(int, input().split())))
func(matrix)