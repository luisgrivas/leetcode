# 26. Remove Duplicates from Sorted Array

[Problem](https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/).Given an integer array nums sorted in non-decreasing order,
remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

TODO EX

```python3
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        current_ind =  0
        next_ind = 1
        n = len(nums)
        while 0 < next_ind < n:
            if nums[current_ind] < nums[next_ind]:
                current_ind += 1
                next_ind += 1
            else:
                nums.pop(current_ind)
                n-=1
        return n
```
