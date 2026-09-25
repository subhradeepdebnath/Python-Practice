def func(matrix):
    max_sum=0
    max_row=0
    for i in range(n):
        total=0
        for j in range(m):
            total+=matrix[i][j]
        if total>max_sum:
            max_sum=total
            max_row=i+1
    print(max_row,max_sum)  
n=int(input())
m=int(input())
matrix=[]
for i in range(n):
    matrix.append(list(map(int,input().split())))
func(matrix)       