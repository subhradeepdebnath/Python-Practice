arr = list(map(int, input().split()))

max = arr[len(arr)-1]
a = []

a.append(max)

for i in range(len(arr)-2, -1, -1):
    if arr[i] > max:
        max = arr[i]
        a.append(arr[i])

a.reverse()

print(*a)