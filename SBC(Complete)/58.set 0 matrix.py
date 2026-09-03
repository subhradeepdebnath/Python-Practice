def func(matrix, r, c):

    zero_row = []
    zero_col = []

    # Pehle 0 ki position find karo
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 0:
                zero_row.append(i)
                zero_col.append(j)

    # Jis row mein 0 mila, usko 0 karo
    for i in zero_row:
        for j in range(c):
            matrix[i][j] = 0

    # Jis column mein 0 mila, usko 0 karo
    for j in zero_col:
        for i in range(r):
            matrix[i][j] = 0

    # Matrix print karo
    for i in range(r):
        print(*matrix[i])


r, c = map(int, input().split())

matrix = []

for i in range(r):
    data = list(map(int, input().split()))
    matrix.append(data)

func(matrix, r, c)