def func(words):
    a=""
    for i in range(len(words)-1,-1,-1):
        a=a+words[i]+" "
    print(a,sep=" ")
arr=input()
words=arr.split()
func(words)