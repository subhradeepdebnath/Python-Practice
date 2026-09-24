def func(matrix,f,s):
    for i in range(len(matrix)):   
        matrix[i][f],matrix[i][s]=matrix[i][s],matrix[i][f] 
    for row in matrix:
        print(*row)
n=int(input())
m=int(input())
matrix=[]
for i in range(n):
    matrix.append(list(map(int,input().split())))
f=int(input())
s=int(input())
func(matrix,f,s)