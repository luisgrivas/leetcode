# 14. Longest Common Prefix

[Problem.](https://leetcode.com/problems/longest-common-prefix/) Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

The solution is rather simple. It consists of two nested for loops. Unfortunately I couldn't find an elegant implementation. 

```python3
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs[0])
        for i in range(n, 0, -1):
            prefix = strs[0][:i]
            flag = 0
            for s in strs[1:]:
                if prefix != s[:i]:
                    flag += 1
                    break
            if flag == 0:
                return prefix     
        return ""
```
