# 3. Longest Substring Without Repeating Characters

[Problem.](https://leetcode.com/problems/longest-substring-without-repeating-characters/description/) 
Given a string s, find the length of the longest substring without repeating characters.

I came up with the following idea. First, given the string s, we calculate how many unique characters it contains. If this number equals the length of s or
if the length of s is less than two, then we return the length of s. This is because if all the characters of s are different, then s is the largest substring;
also, if s has length one or zero, then the only substring that it has is s itself (or the empty string). Now, if all of these fails, then by the 
[Pigeonhole principle](https://en.wikipedia.org/wiki/Pigeonhole_principle) we only have to check substrings with length less than or equal to the number of
unique characters of s. 

Even though this solution is straightforward, it is very slow. Apparently there are better ways to solve this. In the future I will revisit this problem.

```python3
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        k = len(set(s))
        if (n < 2) or (k == n):
            return n
        else:
            for i in range(k, 1, -1):
                for j in range(n-i+1):
                    if len(set(s[j:(i+j)])) == i:
                        return i
            return 1
```
