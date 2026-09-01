#  Given an n*n matrix, check whether it is an symmetric matrix or not?
n=int(input())
matrix= []
for i in range(n):
    data=list(map(int, input().split()))
    matrix.append(data)
found=True
for i in range(n):
    for j in range(n):
        if matrix[i][j]!=matrix[j][i]:
            found=False 
            break
if found:         
    print("symmetric matrix")
else:
    print("Not Symmetric matrix")