def func(n):
    answer=0
    for i in range(1, n+1):
        if i*i==n:
            print(i)
            return
        elif i*i<n:
            answer=i
        else:
            break
    print(answer)
n=int(input())
func(n)
