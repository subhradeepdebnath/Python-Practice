def words(s):
    count=1
    for ch in s:
        if ch == " ":
            count+=1
    print(count)
s=input()
words(s)