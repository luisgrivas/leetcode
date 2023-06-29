# 22. Generate Parentheses

[Problem](https://leetcode.com/problems/generate-parentheses/description/) Given n pairs of parentheses, write a function to generate 
all combinations of well-formed parentheses.


TODO EXP (Dyck words)

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        pref_list = [('', 0, 0)]
        dyck = []
        while pref_list:
            pref, lp, rp = pref_list.pop()
            if lp == rp == n:
                dyck.append(pref)
            else:
                if rp < lp:
                    pref_list.append((pref + ')', lp, rp + 1))      
                if lp < n:
                    pref_list.append((pref + '(', lp + 1, rp))       
        return dyck
```
