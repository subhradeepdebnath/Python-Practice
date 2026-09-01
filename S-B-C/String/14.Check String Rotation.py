# Check String Rotation
s=input()
n=input()
a=""
if len(s)!=len(n):
    print("not rotation")
else:
    a=s+s
if n in a:
    print("rotation")
else:
    print("not")
    
        