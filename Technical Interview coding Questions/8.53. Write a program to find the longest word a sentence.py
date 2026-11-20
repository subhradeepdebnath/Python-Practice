def func(words):
    longest=""
    for i in range(len(words)):
        if len(words[i]) > len(longest) :
            longest=words[i]
    print(longest)
arr=input()
words=arr.split()
func(words)