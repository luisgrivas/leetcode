# 96. Unique Binary Search Trees

[Problem](https://leetcode.com/problems/unique-binary-search-trees/). Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly
n nodes of unique values from 1 to n.

## Solution
It is a standard result in combinatorics (see for instance this [wikipedia](https://en.wikipedia.org/wiki/Catalan_number#Applications_in_combinatorics) note) that the number of unique binary search trees on $n$ vertices, is given by the nth Catalan number:
$$C_n = \frac{1}{n+1} \cdot {2n \choose n} $$

It can be shown (by induction on $n$), that the Catalan numbers satisfy the following recursion formula:

$$C_n = \frac{2 (2 n - 1)}{n+1} \cdot C_{n-1}.$$

With these results, we can implement the following solutions.

## Code
Without using recursion and using the ```math``` module:

```python
from math import comb
class Solution:
    def numTrees(self, n: int) -> int:
        return int(catalan_n = (comb(2*n, n) / (n + 1)))
```

Applying recursion:

```python
class Solution:
    def numTrees(self, n: int) -> int:
        if n == 1:
            return 1    
        previous_catalan = self.numTrees(n-1)
        return int(previous_catalan * (4*n - 2) / (n + 1))
```

