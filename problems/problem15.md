# 15. 3Sum

[Problem](https://leetcode.com/problems/3sum/description/) Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.


```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hmap = {val:ind for ind, val in enumerate(nums) }
        length = len(nums)
        triplets = set()

        for i in range(length - 1):
            for j in range(i+1, length):
                ssum = -(nums[i] + nums[j])
                if ssum in hmap:
                    k = hmap[ssum]
                    if (k != i) and (k != j):
                        triplets.add( tuple(sorted((nums[i], nums[j], nums[k]))))

        return triplets
```

FALTAN OTRAS SOLUCIONES EFICIENTES...