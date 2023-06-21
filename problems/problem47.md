# 47. Permutations II

[Problem](https://leetcode.com/problems/permutations-ii/description/). Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.


> This is slow...
```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        permutations = list()
        
        def tree(current, options):
            if not options:
                permutations.append(current)
                return
            else:
                for ind, val in enumerate(options):
                    new = current + [val]
                    if new not in permutations:
                        tree(current + [val], options[:ind] + options[(ind + 1):])
        
        tree([], nums)

        return permutations
```