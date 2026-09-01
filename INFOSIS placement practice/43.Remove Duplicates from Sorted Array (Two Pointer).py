# Remove Duplicates from Sorted Array (Two Pointer)

n = int(input())
arr = list(map(int, input().split()))

j = 0

for i in range(1, n):
    if arr[i] != arr[j]:
        j += 1
        arr[j] = arr[i]

print(*arr[:j+1])