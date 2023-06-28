# 18. 4Sum

[Problem](https://leetcode.com/problems/4sum/description/). Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

* 0 <= a, b, c, d < n
* a, b, c, and d are distinct.
* nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order.



```python
class Solution:
    def threeSum(self, nums: List[int], target: int) -> List[List[int]]:
        hmap = {val:ind for ind, val in enumerate(nums) }
        length = len(nums)
        triplets = set()

        for i in range(length - 1):
            for j in range(i+1, length):
                ssum = target - (nums[i] + nums[j])
                if ssum in hmap:
                    k = hmap[ssum]
                    if (k != i) and (k != j):
                        triplets.add( tuple(sorted((nums[i], nums[j], nums[k]))))

        return triplets

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        quads = set()
        for ind, val in enumerate(nums):
            triplets = self.threeSum(nums[(ind+1):], target - val)
            for t in triplets:
                i,j,k = t     
                quads.add(tuple(sorted([val, i, j, k])))
        
        return quads
```

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        """ assuming nums is already sorted"""
        pairs = set()
        left = 0
        right = len(nums) - 1
        while left < right:
            leftValue = nums[left]
            rightValue = nums[right]
            ssum = leftValue + rightValue
            if ssum  == target:
                pairs.add((leftValue, rightValue))
                right -= 1
                left += 1
            elif ssum > target:
                right -= 1
            else:
                left += 1
        return pairs

    
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        quads = set()
        nums = sorted(nums)     
        for i, numi in enumerate(nums[:-3]):
            for j, numj in enumerate(nums[(i+1):-2]):
                pairs = self.twoSum(nums[(i + j + 2):], target - numi - numj)
                for p in pairs:
                    val1, val2 = p
                    quads.add((numi, numj, val1, val2))
        return quads
```