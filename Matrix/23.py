#  Given an m × n matrix, print all elements in spiral order.
row, col=map(int, input().split())
matrix=[]
for i in range(row):
    data= list(map(int, input().split()))
    matrix.append(data)
top =0
button=row-1
left=0
right= col-1
while top <= bottom and left <= right:

    for i in range(left, right + 1):
        print(matrix[top][i], end=" ")
    top += 1

    
    for i in range(top, bottom + 1):
        print(matrix[i][right], end=" ")
    right -= 1

    
    if top <= bottom:
        for i in range(right, left - 1, -1):
            print(matrix[bottom][i], end=" ")
        bottom -= 1

    if left <= right:
        for i in range(bottom, top - 1, -1):
            print(matrix[i][left], end=" ")
        left += 1