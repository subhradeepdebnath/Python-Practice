# Print a Hollow Inverted Right-Angled Triangle?
n=int(input())
for i in range(n,0,-1):
    for j in range(n):
        if i == 0 or j == 0 or j == n-i-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
    