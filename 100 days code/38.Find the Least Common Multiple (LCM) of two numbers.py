# Find the LCM of two numbers

a = int(input())
b = int(input())

lcm = max(a, b)

while True:
    if lcm % a == 0 and lcm % b == 0:
        break
    lcm += 1
print(lcm)