def func(s):
    count=0
    cout=0
    for ch in s:
        if ch.isalpha():
            if ch.lower()  in "aeiou":
                count+=1
            else:
                cout+=1
    print("vowels", count)
    print("consonant",cout)
s=input()
func(s)