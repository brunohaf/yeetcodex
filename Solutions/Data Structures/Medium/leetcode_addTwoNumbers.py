"""
Source: https://leetcode.com/problems/add-two-numbers/
"""

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def parseInt(self, headNode: Optional[ListNode]) -> int:
        vals = f"{headNode.val}"
        node = headNode.next
        while (node is not None):
            vals = f"{node.val}{vals}"
            node = node.next
        return int(vals)

    def fromInt(self, integer: int) -> Optional[ListNode]:
        nodes = [ListNode(int(c)) for c in str(integer)]
        head = nodes.pop()
        node = head
        while len(nodes):
            node.next = nodes.pop()
            node = node.next
        return head

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        _sum = self.parseInt(l1) + self.parseInt(l2)
        return self.fromInt(_sum)
