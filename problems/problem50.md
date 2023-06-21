# 50. Pow(x, n)
[Problem](https://leetcode.com/problems/powx-n/description/). Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

It seems that the direct implementation is not efficient, resulting in slow performance. The key lies in employing recursion: dividing the exponent in halves and multiplying the intermediate results. Here's a Python solution that utilizes this approach.

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        
        if n < 0:
            n = -n 
            x = 1 / x
        
        rest = self.myPow(x, n // 2)
        if n % 2 == 0:
            return rest * rest
        
        return x * rest * rest 
```

By implementing recursion and employing the divide-and-conquer technique, we can optimize the performance of the power calculation.