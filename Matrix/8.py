#  Given an m × n matrix, print the sum of every row?
row,col=map(int,input().split())
matrix=[]
for i in range(row):
    data=list(map(int,input().split()))
    matrix.append(data)
for i in matrix:
    sum=0
    for j in i:
        sum=sum+j
    print(sum)