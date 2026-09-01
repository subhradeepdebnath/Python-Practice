class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def func(arr, key):

    head = Node(arr[0])
    current = head

    for i in range(1, len(arr)):
        current.next = Node(arr[i])
        current = current.next

    current = head

    while current:

        if current.data == key:
            print(True)
            return

        current = current.next

    print(False)


arr = list(map(int, input().split()))
key = int(input())

func(arr, key)