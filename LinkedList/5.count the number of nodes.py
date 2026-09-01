# Count the number of nodes?
class Node:
    def __init__(self,data):
        self.data= data
        self.next=None
first= Node(10)
second=Node(20)
third=Node(30)
first.next=second
second.next=third
count=0
temp=first
while temp!=None:
    count+=1
    temp=temp.next
print(count)