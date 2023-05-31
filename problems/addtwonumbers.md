# 2. Add Two Numbers

[Problem]. You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Te solution is straighforward once we recall how the sum algorithm works. We need to calculate the sum of values for nodes in the same position. We should also check if this sum exceeds 9, as we would need to carry over a value of 1 to the next sum. We stop the algorithm when we run out of digits to calculate or if there is no carry value of 1 from the previous sum. The python implementation is the following:

```python3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        chain = ListNode(val=-1)
        while l1 or l2 or count > 0:
            current_node = ListNode()
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + count
            count = total // 10
            total = total % 10
            current_node.val = total
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None 
            if chain.val == -1:
                chain = current_node
            else:
                prev_node.next = current_node
            prev_node = current_node
        
        return chain

```