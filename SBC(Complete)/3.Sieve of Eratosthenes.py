# Given an integer N, find and print all prime numbers from 1 to N using the Sieve of Eratosthenes.?

def func(n):
    for i in range(2,n+1):
        prime=True
        for j in range(2,i):
            if i%j==0:
                prime=False
        if prime:
            print(i)
n=int(input())
func(n)


# same as question 2
