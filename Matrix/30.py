#  Given an N × N matrix, print all the main diagonal elements
n=int(input())
matrix= []
for i in range(n):
    data=list(map(int, input().split()))
    matrix.append(data)
    val=[]
for i in range(n):
        val.append(matrix[i][i])
print(val)