def func(s, k ):
    maximum=0
    for i in range(len(s)):
        a=""
        for j in range(i, len(s)):
            if s[j]not in a:
                if len(a) >= k:
                    break
                a=a+s[j]
            length=j-i+1

            if length>maximum:
                maximum=length
    print(maximum)
s=input()
k=int(input())
func(s,k)

