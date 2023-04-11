# 5. Longest Palindromic Substring

[Problem.](https://leetcode.com/problems/longest-palindromic-substring/description/) Given a string s, return the longest palindromic [substring](https://en.wikipedia.org/wiki/Substring) in s.

A very simple solution is to find all the possible substrings of s starting with the longest (the string s itself) and continue with second longest and so on. 
In each iteration we check if the substring is palindromic. Notice that this procedure ends since a character is always a palindromic substring. 

```python3
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        for i in range(n, 0, -1):
            for j in range(n-i+1):
                subs = s[j:(i+j)]
                if subs == subs[::-1]:
                    return subs

```
