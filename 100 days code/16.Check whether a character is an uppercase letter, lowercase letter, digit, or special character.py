# Check whether a character is an uppercase letter, lowercase letter, digit, or special character?
ch=input()
if ch>='A' and ch<='Z':
    print("upperCase")
elif ch >='a' and ch<='z':
    print("lowercase")
elif ch >='0' and ch<='9':
    print("digit")
else:
    print("Special Character")
    