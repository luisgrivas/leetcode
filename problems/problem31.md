# 31. Next Permutation
[Problem](). Given an array of integers nums, find the next permutation of nums.


```python
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lengthNums = len(nums)
        pointer = lengthNums - 2

        while pointer >= 0:
            pointerValue = nums[pointer]
            if pointerValue < nums[pointer + 1]:
                rest = nums[pointer + 1:]
                subsValue = min([num for num in rest if num > pointerValue])
                rest.remove(subsValue)
                rest.append(pointerValue)
                rest = sorted(rest)
                nums[pointer] = subsValue

                for i in range(pointer + 1, lengthNums):
                    nums[i] = rest[i - pointer - 1]

                break
            pointer -= 1
        
        if pointer < 0:
            for i in range(lengthNums // 2):
                value1 = nums[i]
                value2 = nums[-i-1]
                nums[i] = value2
                nums[-i-1] = value1
```