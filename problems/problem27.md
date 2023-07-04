# 27. Remove Element

[Problem](https://leetcode.com/problems/remove-element/description/). Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
TODO EXP

```python3
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        n = len(nums)
        i = 0
        while i < n:
            el = nums[i]
            if el == val:
                nums.pop(i)
                n-=1
            else:
                i+=1
        return i
```

```python3
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)
```
