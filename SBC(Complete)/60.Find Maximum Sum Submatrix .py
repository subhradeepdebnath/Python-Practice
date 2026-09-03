def func(matrix, r, c):
    maximum = matrix[0][0]

    for top in range(r):
        temp = [0] * c

        for bottom in range(top, r):
            for j in range(c):
                temp[j] += matrix[bottom][j]

            curr = temp[0]

            if curr > maximum:
                maximum = curr

            for j in range(1, c):
                if curr + temp[j] > temp[j]:
                    curr = curr + temp[j]
                else:
                    curr = temp[j]

                if curr > maximum:
                    maximum = curr

    print(maximum)


r, c = map(int, input().split())

matrix = []

for i in range(r):
    data = list(map(int, input().split()))
    matrix.append(data)

func(matrix, r, c)