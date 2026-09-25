def func(matrix,target):
    for i in range(n):   
        for j in range(m):   
            if matrix[i][j]==target:   
                print(i+1,j+1)  
                return  

    print("Not Found")   

n=int(input())
m=int(input())
matrix=[]
for i in range(n):
    matrix.append(list(map(int,input().split())))
target=int(input())
func(matrix,target)