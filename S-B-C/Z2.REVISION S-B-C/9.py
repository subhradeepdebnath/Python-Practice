def func(s):
    visited=[]
    for ch in s:
        if ch not in visited:
            count=s.count(ch)
            print(f"{ch}: {count}")
            visited.append(ch)
s=input()
func(s)