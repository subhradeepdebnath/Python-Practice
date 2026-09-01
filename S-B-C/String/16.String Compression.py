s = input()
a = ""
count = 1

for i in range(len(s)-1):
    if s[i] == s[i+1]:
        count += 1
    else:
        a = a + s[i] + str(count)
        count = 1

a = a + s[len(s)-1] + str(count)

print(a)