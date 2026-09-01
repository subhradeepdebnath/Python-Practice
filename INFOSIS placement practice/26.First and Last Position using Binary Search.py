n = int(input())
arr = list(map(int, input().split()))
key = int(input())

# Find First Occurrence
low = 0
high = n - 1
first = -1

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == key:
        first = mid
        high = mid - 1      # Search on left side
    elif arr[mid] < key:
        low = mid + 1
    else:
        high = mid - 1

# Find Last Occurrence
low = 0
high = n - 1
last = -1

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == key:
        last = mid
        low = mid + 1       # Search on right side
    elif arr[mid] < key:
        low = mid + 1
    else:
        high = mid - 1

print(first, last)