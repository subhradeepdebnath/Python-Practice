#  Given two matrices of the same size, add them and print the resultant matrix?
r=int(input())
c=int(input())
a=[]
b=[]
sum_matrix=[]
for i in range(r):
    row=list(map(int,input().split()))
    a.append(row)
for i in range(r):
    row = list(map(int,input().split()))
    b.append(row)
for i in range(r):
    row=[]
    for j in range(c):
        row.append(a[i][j]+ b[i][j])
    sum_matrix.append(row)
for i in range(r):
    for j in range(c):
        print(sum_matrix[i][j], end=" ")
    print()