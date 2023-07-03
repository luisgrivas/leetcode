# 19. Remove Nth Node From End of List
[Problem](https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/). Given the head of a linked list, remove the nth node from the end of the list and return its head.


```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tail = head
        hmap = {0:head}
        ind = 0
        while tail.next:
            ind += 1
            tail = tail.next
            hmap[ind] = tail       

        subsInd = ind - n + 1

        if ind == 0:
            return None
        
        if subsInd == 0:
            return hmap[1]
        
        if subsInd == ind:
            hmap[subsInd - 1].next = None
            return head
        
        hmap[subsInd - 1].next = hmap[subsInd + 1]
        return head  
```
