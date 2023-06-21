# 66. Plus One

[Problem](https://leetcode.com/problems/plus-one/description/). You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.


```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        count = 1
        for ind in reversed(range(len(digits))):
            if count == 0: break
            digits[ind] += count
            count = digits[ind] // 10
            digits[ind] %= 10 

        if count > 0:
            digits.insert(0, 1)
        return digits
```