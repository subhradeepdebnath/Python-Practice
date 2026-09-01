#  Given an N × N (square) matrix, find the sum of the primary diagonal elements.

n=int(input())
matrix=[]
for i in range(n):
    data=list(map(int, input().split()))
    matrix.append(data)
sum=0
for i in range(n):
    sum=sum+matrix[i][i]
print(sum)