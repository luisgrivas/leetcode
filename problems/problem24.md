# 24. Swap Nodes in Pairs

[Problem](https://leetcode.com/problems/swap-nodes-in-pairs/). Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)



```python
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        hmap = {0:head}
        tailNode = head
        ind = 0
        while tailNode.next:
            tailNode = tailNode.next
            ind += 1
            if ind % 2 == 1:
                hmap[ind] = hmap[ind -1]
                hmap[ind - 1] = tailNode
            else:
                hmap[ind] = tailNode

        for k in hmap:
            hmap[k].next = hmap.get(k+1, None)

        return hmap[0]
```