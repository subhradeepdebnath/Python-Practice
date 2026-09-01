s=input()
n=input()
count=0
for i in range(len(s)-len(n)+1):
    if s[i:i+len(n)]==n:
        count+=1
print(count)