#  given an m*n matrix, find the sum of all the elements in the matrix.
row, col=map(int, input().split())
matrix=[]
sum=0
for i in range(row):
    data= list(map(int, input().split()))
    matrix.append(data)
for i in matrix:
    for j in i:
        sum=sum+j
print(sum)