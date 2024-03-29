# 46. Permutations

[Problem](https://leetcode.com/problems/permutations/description/). Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

## Solution
This problem can be solved using [backtracking](https://en.wikipedia.org/wiki/Backtracking#). 

## Code
```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        def backtrack(current, options):
            if not options:
                permutations.append(current[:])
                return
            
            for ind, val in enumerate(options):
                current.append(val)
                new_options = options[:ind] + options[ind+1:]
                backtrack(current, new_options)
                current.pop()
        backtrack([], nums)
        return permutations
```
