arr=list(map(int, input().split()))
target=int(input())
for i in range(len(arr)-1,-1,-1):
    if target==arr[i]:
        print(i)
        break
    