# 46. Permutations

[Problem](https://leetcode.com/problems/permutations/description/). Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.


```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = list()
        
        def tree(current, options):
            if options:
                for ind, val in enumerate(options):
                    tree(current + [val], options[:ind] + options[(ind + 1):])
            else:
                permutations.append(current)
                return
        
        tree([], nums)

        return permutations
```