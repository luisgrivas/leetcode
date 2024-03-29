# 442. Find All Duplicates in an Array

[Problem](https://leetcode.com/problems/find-all-duplicates-in-an-array/description/) Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in $O(n)$ time and uses only constant extra space.


## Solution
If we omit the restrictions, we can make use of a hash table (this violates the constant extra space restriction) to count the frequency of the elements in $nums$.

```python
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hash_map = {num:0 for num in nums}
        for num in nums:
            hash_map[num] += 1
        duplicates = []
        for num, count in hash_map.items():
            if count > 1:
                duplicates.append(num)
        return duplicates
```

We can approach this problem differently by considering the array `nums` as a mapping function, denoted as $f$, from the set $[n]$ to itself. The solution involves identifying all numbers that satisfy $f(i) = f(j)$ where $i \neq j$. This can be achieved in linear time.

To implement this, iterate through each element of the set $[n]$ and multply the image by -1. If $f(i)$ is already less than 0, it indicates a duplicate number, which we save in a list. Here's the Python implementation:

```python
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []
        for i in range(len(nums)):
            num = abs(nums[i])
            if nums[num - 1] < 0:
                duplicates.append(num)
            nums[num - 1] *= -1
        return duplicates
```
