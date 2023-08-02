# 95. Unique Binary Search Trees II

[Problem](https://leetcode.com/problems/unique-binary-search-trees-ii/). Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from copy import deepcopy
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        def aux(labels):
            if len(labels) == 0:
                return []
            elif len(labels) == 1:
                return [TreeNode(labels[-1])]
            else:
                output = []
                for ind, label in enumerate(labels):
                    left_labels = labels[:ind]
                    right_labels = labels[(ind+1):]
                    left_tree_list = aux(left_labels)
                    right_tree_list = aux(right_labels)
                    if not left_tree_list:
                        for root in right_tree_list:
                            output.append(TreeNode(label, right=root))
                    elif not right_tree_list:
                        for root in left_tree_list:
                            output.append(TreeNode(label, left=root))
                    else:
                        for left_root in left_tree_list:
                            for right_root in right_tree_list:
                                output.append(TreeNode(label, left=left_root, right=right_root))
            return output

        bbt_list = aux(list(range(1, n+1)))
        return bbt_list
```