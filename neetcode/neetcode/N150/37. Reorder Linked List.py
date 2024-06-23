# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next




class Solution:
    # def reorderList(head: ListNode) -> None:
    #     p1 = head
    #     while p1.next and p1.next.next:
    #         last_node, p2 = p1, p1
    #         while last_node.next and last_node.next.next:
    #             last_node = last_node.next
    #             tmp = last_node.next
    #
    #         last_node.next = None
    #         print("last node", tmp.val)
    #         tmp.next = p2.next
    #         p2.next = tmp
    #         print("new head" ,p2.val)
    #         p1 = p1.next.next
    #     printNodes(head)
    # def reorderList(head: ListNode) -> None:
    #     p1 = head
    #     while p1.next and p1.next.next:
    #         last_node = p1
    #         while last_node.next and last_node.next.next:
    #             last_node = last_node.next
    #
    #         tmp = last_node.next
    #         last_node.next = None
    #         print("last node", tmp.val)
    #         tmp.next = p1.next
    #         p1.next = tmp
    #         print("new head" ,p1.val)
    #         p1 = p1.next.next
    #     printNodes(head)
    def reorderList(head: ListNode) -> None:
        p1 = head
        while head.next and head.next.next:
            last_node = head
            while last_node.next and last_node.next.next:
                last_node = last_node.next

            tmp = last_node.next
            last_node.next = None
            print("last node", tmp.val)
            tmp.next = head.next
            head.next = tmp
            print("new head" ,head.val)
            head = head.next.next
        printNodes(p1)



def printNodes( h: ListNode):
    while h:
        print(h.val)
        h = h.next

values = [1,2,3,4,5,6,7,8]

1,8,2,7,3,6,4,5



head = ListNode()
pointer = head
for v in values:
    newNode = ListNode(v, None)
    pointer.next = newNode
    pointer = pointer.next

head = head.next
# printNodes(head)
Solution.reorderList(head)