# 136. Single Number

[Problem](https://leetcode.com/problems/single-number/). Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

**Note**: You must implement a solution with a linear runtime complexity and use only constant extra space.

Given the constrain that states that the runtime must be linear, the solution should rely on a for loop (or something equivalent). Let's recall the truth table of the ```xor``` operation:
| xor  |  1 | 0 |
| ---- | ---- | ---- |
| 1 | 0 | 1  |
| 0 | 1 | 0  |

From this table, we can observe that for integers ```a``` and ```b```,  ``` a xor b  = 0 ``` if and only if ```a = b```. Therefore, the solution involves calculating the xor of all the elements of the input list. The resulting value will correspond to the element that appears only once. 

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unique = 0
        for num in nums:
            unique ^= num
        return unique
```