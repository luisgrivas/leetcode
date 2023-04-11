# 5. Longest Palindromic Substring

[Problem.](https://leetcode.com/problems/longest-palindromic-substring/description/) Given a string s, return the longest palindromic [substring](https://en.wikipedia.org/wiki/Substring) in s.

A naive solution is to find all the possible substrings of s starting with the longest (the string s itself) and continue with second longest and so on. 
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

There is another approach to solve this problem. First, we need some notation. Let $s$ be a string and denote by $s[i,j]$ the substring with initial index $i$ and final index $j$. Let $S = (s_{i,j})$ be a matrix with $s_{i,j} = 1$ if the substring $s[i,j]$ is palindromic and $0$ otherwise. Notice that $S$ is symmetric and its diagonal consists only of ones (since every substring of length one is palindromic). Also, and this is the interesting part, $S$ satisfies the following recursion rule:

$$s_{i,j} = (s[i] == s[j]) \cdot s_{i+1,j-1}.$$

With this in mind, we have the following solution

```python3
class Solution:
    def longestPalindrome(self, s: str) -> str:
       pass
```
