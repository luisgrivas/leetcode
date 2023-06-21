# 58. Length of Last Word
[Problem](https://leetcode.com/problems/length-of-last-word/). Given a string s consisting of words and spaces, return the length of the last word in the string.


```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for el in s[::-1]:
            if el == ' ':
                if count > 0: break
            else: count += 1
        return count
```

```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
````