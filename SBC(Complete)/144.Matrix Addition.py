def func(matrix1,matrix2):
    result=[]
    for i in range(n):
        row=[]
        for j in range(m):
            row.append(matrix1[i][j]+matrix2[i][j])
        result.append(row)
    for row in result:
        print(*row)
n=int(input())
m=int(input())

matrix1=[]
for i in range(n):
    matrix1.append(list(map(int,input().split())))

matrix2=[]
for i in range(n):
    matrix2.append(list(map(int,input().split())))

func(matrix1,matrix2)