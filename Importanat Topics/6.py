#  you are given a list of point and must visit all the remaining points in order.
n=int(input())
points=[]
for i in range(n):
    x,y = map(int, input().split())
    points.append([x,y])
time=0
for i in range(n-1):
    x1=points[i][0]
    y1=points[i][1]
    x2=points[i+1][0]
    y2=points[i+1][1]
    dx=abs(x2-x1)
    dy=abs(y2-y1)
    time=time+max(dx,dy)
print(time)


 