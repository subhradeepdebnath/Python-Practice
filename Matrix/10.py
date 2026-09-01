#  Given an m × n matrix, count how many even and odd elements are present.
row,col=map(int, input().split())
matrix=[]
for i in range (row):
    data=list(map(int, input().split()))
    matrix.append(data)
even_count=0
odd_count=0
for i in matrix:
    for j in i:
        if j%2==0:
            even_count+=1
        else:
            odd_count+=1
print(even_count)
print(odd_count)