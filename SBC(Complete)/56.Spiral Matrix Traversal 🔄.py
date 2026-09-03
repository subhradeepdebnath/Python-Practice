def func(matrix, r, c):
    top=0
    bottom=r-1
    left=0
    right=c-1
    result=[]
    while top<= bottom and left <=right:
        for i in range(left, right+1):
            result.append(matrix[top][i])
        top+=1
        
        for i in range(top, bottom+1):
            result.append(matrix[i][right])
        right-=1
        
        if top<=bottom:
            for i in range(right, left-1, -1):
                result.append(matrix[bottom][i])
            bottom-=1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])

            left += 1               # left column complete

    print(*result)


r, c = map(int, input().split())     # rows aur columns

matrix = []

for i in range(r):
    data = list(map(int, input().split()))
    matrix.append(data)

func(matrix, r, c)