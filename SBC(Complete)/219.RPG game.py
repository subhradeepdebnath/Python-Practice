def func(n,k,arr1,arr2):
    count=0
    for i in range(len(arr1)):
            if k>=arr1[i]:
                k+=arr2[i]
                count+=1
            else:
                count+=0
    print(count)
            
n=int(input())
k=int(input())
arr1=[int(input())for i in range(n)]
arr2=[int(input())for i in range(n)]
func(n,k,arr1,arr2)