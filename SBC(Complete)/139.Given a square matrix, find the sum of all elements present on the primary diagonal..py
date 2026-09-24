def func(matrix):
    sum=0
    for i in range(len(matrix)):
            sum+=matrix[i][i]
    print(sum)
n=int(input())
m=int(input())
matrix=[]
for i in range(n):
    matrix.append(list(map(int, input().split())))
func(matrix)