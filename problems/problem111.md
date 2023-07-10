# 111. Minimum Depth of Binary Tree

[Problem](https://leetcode.com/problems/minimum-depth-of-binary-tree/description/). Given a binary tree, find its minimum depth.

The solution involves exploring the binary tree using a breadth-first search. If we encounter a node that has no children (neither left nor right), then the node is a leaf, and we return the current depth. Otherwise, we continue expanding the nodes. This procedure is guaranteed to terminate since the tree has finite depth.

```python
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        currentDepth = [root] if root else []
        depth = 0
        while currentDepth:
            depth += 1
            currentDepth = [(node.left, node.right) for node in currentDepth]
            if (None, None) in currentDepth:
                return depth
            currentDepth = (
                [node[0] for node in currentDepth if node[0] is not None] + 
                [node[1] for node in currentDepth if node[1] is not None]
            )
        return depth
```