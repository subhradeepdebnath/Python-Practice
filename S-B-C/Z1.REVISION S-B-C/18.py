def check(s):
    for ch in s:
        if ch < "0" or ch > "9":
            print("false")
            return
    print(True)
s=input()
check(s)