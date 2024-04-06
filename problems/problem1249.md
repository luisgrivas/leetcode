# 1249. Minimum Remove to Make Valid Parentheses

[Problem.](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/) 
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

* It is the empty string, contains only lowercase characters, or
* It can be written as AB (A concatenated with B), where A and B are valid strings, or
* It can be written as (A), where A is a valid string.

# Solution
TODO EX

```python
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        n_left_p, n_right_p  = 0, 0
        n_left_ind, n_right_ind, new_s  = [], [], []

        for i, c in enumerate(s): 
            if c == '(':
                n_left_p += 1
                n_left_ind.append(i)
                new_s.append('')
            elif c == ')':
                if n_left_p > n_right_p:
                    n_right_p += 1
                    ind = n_left_ind.pop(-1)
                    new_s[ind] = s[ind]
                    new_s.append(c)
                else:
                    n_right_ind.append(i)
                    new_s.append('')
            else:
                new_s.append(c)
        return ''.join(new_s)
```
