# Valid Parentheses
s=input()

stack=[]
pair={')':'(', '}':'{', ']':'['}

for i in s:
    if i in "({[":
        stack.append(i)
    elif not stack or stack.pop()!=pair[i]:
        print("NO")
        break
else:
    print("YES" if not stack else "NO")
    