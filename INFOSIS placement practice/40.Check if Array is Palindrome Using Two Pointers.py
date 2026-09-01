# Check if Array is Palindrome Using Two Pointers

n = int(input())
arr = list(map(int, input().split()))

left = 0
right = n - 1

palindrome = True

while left < right:
    if arr[left] != arr[right]:
        palindrome = False
        break

    left += 1
    right -= 1

if palindrome:
    print("Palindrome")
else:
    print("Not Palindrome")