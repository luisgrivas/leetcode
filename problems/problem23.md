# 23. Merge k Sorted Lists

[Problem](https://leetcode.com/problems/merge-k-sorted-lists/description/). You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Divide and conquer is a powerful and commonly used paradigm in programming, and it can also be applied to solve this problem. The approach involves dividing the list of nodes into smaller subproblems, sorting each subproblem individually, and then merging the sorted results to obtain the final merged array.

To implement this solution, we start by dividing the list of nodes into two halves, utilizing the divide step. Next, we recursively apply the sorting process to each half, sorting them independently. This conquer step involves solving smaller instances of the problem. Once the two halves are sorted, we merge them together by comparing the elements from each half and placing them in the correct order.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if n == 0:
            return 
        if n == 1:
            return lists[0]
        if n == 2:
            list1 = lists[0]
            list2 = lists[1]
            head = prev = ListNode()

            while list1 and list2:
                val1 = list1.val 
                val2 = list2.val
                if val1 < val2:
                    current = ListNode(val=val1)
                    list1 = list1.next
                else:
                    current = ListNode(val=val2)
                    list2 = list2.next
                
                prev.next = current
                prev = current
            
            if not list1:
                prev.next = list2
            else:
                prev.next = list1
            return head.next
        
        half = n // 2
        sort1 = self.mergeKLists(lists[:half])
        sort2 = self.mergeKLists(lists[half:])
        return self.mergeKLists([sort1, sort2])
```