#  given a string, print the frequency(count) of each character?
n=input()
ss=""
count=0
for ch in n:
    if ch not in ss:
        print(ch, ":" , n.count(ch))
        ss=ss+ch

