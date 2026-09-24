def func(matrix):
    sum=0
    n=len(matrix)
    for i in range(n):   
        sum+=matrix[i][n-1-i]   
    print(sum)

n=int(input())
m=int(input())
matrix=[]
for i in range(n):
    matrix.append(list(map(int,input().split())))
func(matrix)