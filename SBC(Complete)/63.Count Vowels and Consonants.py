def func(s):
    count=0
    cout=0
    for ch in s:
        if ch in "aeiou":
            count+=1
        else:
            cout+=1
    print("vowel:", count)
    print("consonant:", cout)
s=input()
func(s)