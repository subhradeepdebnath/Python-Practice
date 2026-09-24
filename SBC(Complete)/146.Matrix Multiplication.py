def func(matrix1,matrix2):
    result=[]
    for i in range(n):
        row=[]
        for j in range(p):
            total=0
            for k in range(m):
                total+=matrix1[i][k]*matrix2[k][j]
            row.append(total)
        result.append(row)
    for row in result:
        print(*row)
n=int(input())
m=int(input())

matrix1=[]
for i in range(n):
    matrix1.append(list(map(int,input().split())))

m2=int(input())
p=int(input())

matrix2=[]
for i in range(m2):
    matrix2.append(list(map(int,input().split())))

func(matrix1,matrix2)