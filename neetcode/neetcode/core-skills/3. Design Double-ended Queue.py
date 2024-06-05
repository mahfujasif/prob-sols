


class Node:
    def __init__(self, val):
        self.val = val
        self.next  =None
        self.prev = None

class Deque:

    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        new_node = Node(value)
        last_node = self.tail.prev

        last_node.next = new_node
        new_node.prev = last_node
        new_node.next = self.tail
        self.tail.prev = new_node

    def appendleft(self, value: int) -> None:
        new_node = Node(value)
        first_node = self.head.next

        first_node.prev = new_node
        new_node.next = first_node
        self.head.next = new_node
        new_node.prev = self.head

    def pop(self) -> int:
        if self.isEmpty():
            return -1

        del_node = self.tail.prev
        value = del_node.val

        prev_node = del_node.prev
        prev_node.next = self.tail
        self.tail.prev = prev_node
        return value

    def popleft(self) -> int:
        if self.isEmpty():
            return -1

        del_node = self.head.next
        value = del_node.val

        next_node = del_node.next
        self.head.next = next_node
        next_node.prev = self.head
        return value


