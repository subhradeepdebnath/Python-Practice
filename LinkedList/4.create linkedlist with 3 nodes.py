#  create a linked list with 3 nodes?
class Node:
    def __init__(self,data):
        self.data=data
        self.next=Node
first=Node(10)
second=Node(20)
third=Node(30)
first.next=second
second.next=third
print(first.data)
print(first.next.data)
print(second.next.data)