#  given a list of numbers, find the second largest element?
n=list(map(int,input().split()))
large=n[0]
sec=n[0]
for i in n:
    if i > large:
        sec = large
        large =i 
    elif i>sec and i!=large:
        sec= i
print (sec)