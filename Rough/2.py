# //Number of 1 Bits (Hamming Weight)
def func(n):
    a=bin(n)
    count=0
    for i in range(len(a)):
        if a[i]=="1":
            count+=1
    print(count)
n=int(input())
func(n)