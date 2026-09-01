#  #  Given an m*n matrix, check whether it is a Sparse Matrix or not.
row, col=map(int, input().split())
matrix= []
for i in range(row):
    data=list(map(int, input().split()))
    matrix.append(data)
count=0
num=0
for i in range(row):
    for j in range(col):
        if matrix[i][j]==0:
            count+=1
        else:
            num+=1
if count>num:        
    print("Sparse matrix")
else:
    print("Not Sparse matrix")