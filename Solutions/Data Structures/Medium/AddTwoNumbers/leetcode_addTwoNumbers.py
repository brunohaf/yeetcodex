"""
Source: https://leetcode.com/problems/add-two-numbers/
---

Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:

- The number of nodes in each linked list is in the range [1, 100].
- `0 <= Node.val <= 9`
- It is guaranteed that the list represents a number that does not have leading zeros.
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
