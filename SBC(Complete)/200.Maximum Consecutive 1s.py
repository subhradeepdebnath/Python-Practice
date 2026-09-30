def func(arr):

    max = 0
    count = 0

    for i in range(len(arr)):

        if arr[i] == 1:
            count += 1

            if count > max:
                max = count

        else:
            count = 0

    print(max)

arr = list(map(int, input().split()))

func(arr)