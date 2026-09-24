def func(matrix):
    pos=0
    neg=0
    z=0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j]>0:
                pos+=1
            elif matrix[i][j]==0:
                z+=1
            else:
                neg+=1
    print(pos, neg, z)    
n=int(input())
m=int(input())
matrix=[]
for i in range(n):
    matrix.append(list(map(int, input().split())))
func(matrix)