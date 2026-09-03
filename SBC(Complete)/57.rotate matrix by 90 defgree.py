def func(matrix, r, c):
    result = []

    for j in range(c):
        for i in range(r - 1, -1, -1):
            result.append(matrix[i][j])

    index = 0

    for i in range(c):
        for j in range(r):
            print(result[index], end=" ")
            index += 1
        print()


r, c = map(int, input().split())

matrix = []

for i in range(r):
    data = list(map(int, input().split()))
    matrix.append(data)

func(matrix, r, c)