# 16. 3Sum Closest

[Problem](https://leetcode.com/problems/3sum-closest/description/). Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
Return the sum of the three integers.
 

```python
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        length = len(nums)
        ssum = None
        bestDiff = float('inf')

        for ind, val in enumerate(nums):
            left = ind + 1
            right = length - 1
            currentTarget = target - val
            while left < right:
                currentDiff = currentTarget - nums[left] - nums[right]
                
                if abs(currentDiff) < abs(bestDiff):
                    ssum = nums[left] + nums[right] + val
                    bestDiff = currentDiff

                if currentDiff < 0:
                    right -= 1
                else:
                    left += 1
        return ssum
```