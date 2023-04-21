# 7. Reverse Integer

[Problem.](https://leetcode.com/problems/reverse-integer/) Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range $[-2^31, 2^31 - 1]$, then return 0. Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Reversing an integer is a recurrent theme in leetcode (see this [problem](https://github.com/luisgrivas/leetcode/blob/main/problems/palindrome.md)). The *difficult* part with this problem is that we have to deal with an inequality. The solution consists of basic arithmetic. 

```python3
class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        sig = 1
        liminf = -214748364.8
        limsup = 214748364.7
        if x < 0:
            x = -x
            sig = -1
        while(x >= 1):
            r = x % 10
            if sig*rev > limsup - r/10 or sig*rev < liminf - r/10:
                rev = 0
                x = 0
            else:
                rev = (rev * 10) + r
                x = int(x / 10)
        return rev*sig
```
