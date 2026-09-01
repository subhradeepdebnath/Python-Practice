#  given a string, remove all duplicate characters while keeping the first occurrence of each character?
s=input()
n=""
for ch in s:
    if ch not in n:
        n=n+ch
print(n)