from typing import Optional


class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     newHead = None
    #     while head.next:
    #         tmp = ListNode(head.val)
    #         tmp.next = newHead
    #         newHead = tmp
    #         head = head.next
    #     print("ii")
    #     return newHead

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, current = None, head
        while current:
            tmp = current.next
            current.next = prev
            prev = current
            current = tmp
        return prev
def pn(h: ListNode):
    st = ""
    while h:
        st += str(h.val) + " "
        h = h.next
    print(st)

vals = [1,2,3,4,5,6,7]
head = tmp = ListNode()
for v in vals:
    tmp.next = ListNode(v)
    tmp = tmp.next
head = head.next

# pn(head)
pn(Solution.reverseList(Solution(),head))


