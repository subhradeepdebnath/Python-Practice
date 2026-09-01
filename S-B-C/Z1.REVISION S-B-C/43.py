class node:

    def __init__(self, data):
        self.data = data
        self.next = None


def func(arr, val):

    head = node(arr[0])
    current = head

    for i in range(1, len(arr)):
        current.next = node(arr[i])
        current = current.next

    if head.data == val:
        head = head.next

    else:
        current = head

        while current.next:

            if current.next.data == val:
                current.next = current.next.next
                break

            current = current.next

    current = head

    while current:
        print(current.data, end=" ")
        current = current.next


arr = list(map(int, input().split()))
val = int(input())

func(arr, val)