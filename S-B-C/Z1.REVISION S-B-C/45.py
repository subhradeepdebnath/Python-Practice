class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def func(arr):

    head = Node(arr[0])
    current = head

    for i in range(1, len(arr)):
        current.next = Node(arr[i])
        current = current.next

    # Reverse
    prev = None
    current = head

    while current:

        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    head = prev

    # Print
    current = head

    while current:
        print(current.data, end=" ")
        current = current.next


arr = list(map(int, input().split()))

func(arr)