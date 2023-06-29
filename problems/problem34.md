# 34. Find First and Last Position of Element in Sorted Array

[Problem](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/).  Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.


```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return [-1, -1]
        midIndex = n // 2
        
        if nums[midIndex] > target:
            return self.searchRange(nums[:midIndex], target)
        elif nums[midIndex] < target:
            indices = self.searchRange(nums[(midIndex + 1):], target)
            if indices[0] < 0:
                return indices
            else:
                return [indices[0] + midIndex + 1, indices[1] + midIndex + 1]
        else:
            leftPointer = rightPointer = midIndex

            while rightPointer < n:
                if nums[rightPointer] == target:  
                    rightPointer += 1
                else:
                    break

            while leftPointer >= 0:
                if nums[leftPointer] == target:
                    leftPointer -= 1
                else:
                    break

            return [leftPointer + 1, rightPointer - 1]
```