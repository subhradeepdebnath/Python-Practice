def func(s):
    stack=[]
    for i in range(len(s)):
        if s[i]=="(" or s[i]=="{" or s[i]=="[":
            stack.append(s[i])
        else:
            if len(stack)==0:
                print("invalid")
                return
            top=stack.pop()
            if s[i]==")" and top!="(":
                print("invalid")
                return
            if s[i]=="}" and top!="{":
                print("invalid")
                return
            if s[i]=="]" and top!="[":
                print("invalid")
                return
    if len(stack)==0:
        print("valid")
    else:
        print("invalid")
s=input()
func(s)