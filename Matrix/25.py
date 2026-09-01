#  given an n*n matrix, check whether it is an identity matrix or not?
n=int(input())
matrix= []
for i in range(n):
    data=list(map(int, input().split()))
    matrix.append(data)
identify=True
for i in range(n):
    for j in range(n):
        if i==j:
            if matrix[i][j]!=1:
                identify=False
        else:
            if matrix[i][j]!=0:
                identify=False
if identify:
    print("identity matrix")
else:
    print("not an identity matrix")