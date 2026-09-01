def balanced(s):
    stack=[]
    for ch in s:
        if ch=="(" or ch=="[" or ch=="{":
            stack.append(ch)
        elif ch==")":
            if len(stack)==0 or stack[-1]!="(":
                return False
            stack.pop()
        elif ch=="]":
            if len(stack)==0 or stack[-1]!="[":
                return False
            stack.pop()

        elif ch=="}":
            if len(stack)==0 or stack[-1]!="{":
                return False
            stack.pop()
    if len(stack)==0:
        return True
    else:
        return False
    

s=input()

if balanced(s):
    print("Balanced")
else:
    print("Not Balanced")