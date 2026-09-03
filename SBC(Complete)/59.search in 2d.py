def func(matrix, r, c, target):

    for i in range(r):
        for j in range(c):
            if matrix[i][j] == target:
                print("Found")
                return

    print("Not Found")


r, c = map(int, input().split())

matrix = []

for i in range(r):
    data = list(map(int, input().split()))
    matrix.append(data)

target = int(input())

func(matrix, r, c, target)