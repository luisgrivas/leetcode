# 35. Search Insert Position

Problem. Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order. You must write an algorithm with O(log n) runtime complexity.

TODO

```python3
class Solution:
	def searchInsert(self, nums: list[int], target: int) -> int:
		index = 0
		while nums:
			mid = len(nums) // 2
			if nums[mid] == target:
				return index + mid
			elif nums[mid] < target:
				nums = nums[(mid + 1):]
				index = index + mid + 1
			else:
				nums = nums[:mid]
		return index
```
