# 6. Zigzag Conversion
[Problem](https://leetcode.com/problems/zigzag-conversion/description/). 

TODO EXP

```python3
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = ['' for i in range(numRows)]
        i = 0
        d = 1
        for ch in s:
            rows[i]+=ch
            i += d
            if i == 0 or i == (numRows-1):
                d *= -1
        return "".join(rows)
```
