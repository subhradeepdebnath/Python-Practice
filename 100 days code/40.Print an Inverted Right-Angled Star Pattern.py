# Print an Inverted Right-Angled Star Pattern?
n=int(input())
for i in range(n,0,-1):
    for j in range(i):
        print("*", end=" ")
    print()