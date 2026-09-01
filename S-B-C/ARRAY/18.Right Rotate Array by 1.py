arr = list(map(int, input().split()))

last = arr[len(arr)-1]
a = []

a.append(last)

for i in range(len(arr)-1):
    a.append(arr[i])

print(*a)