# 21. Merge Two Sorted Lists

[Problem](https://leetcode.com/problems/merge-two-sorted-lists/description/). You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists. Return the head of the merged linked list.

TODO EXP

```python
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merge = prev = ListNode()
        while list1 or list2:
            if list1 is None:
                current = list2
                list2 = None
            elif list2 is None:
                current = list1
                list1 = None
            elif list1.val  < list2.val:
                current = ListNode(val=list1.val, next=list2)
                list1 = list1.next
            else:
                current = ListNode(val=list2.val, next=list1)
                list2 = list2.next

            prev.next = current
            prev = current

        return merge.next
```

```python
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1 
        elif list1.val < list2.val:
            rest = self.mergeTwoLists(list1.next, list2)
            return ListNode(val=list1.val, next=rest)
        else:
            rest = self.mergeTwoLists(list1, list2.next)
            return ListNode(val=list2.val, next=rest)
```