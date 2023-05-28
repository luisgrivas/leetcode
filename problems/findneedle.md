# 28. Find the Index of the First Occurrence in a String

[Problem](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/). Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Since this is a recurrent task in programming, naturaly Python already has a string method for this:
 
 ```python3
def strStr(self, haystack: str, needle: str) -> int:
	return haystack.find(needle)
 ```

But obviusly, the problem is not intended to be solved in this way. One approach to do this is to iterate over the string ```haystack``` and check if there is a match with the string ```needle```:

```python3
def strStr(self, haystack: str, needle: str) -> int:
        size = len(needle)
        for start in range(len(haystack)):
            if needle in haystack[start:(start + size)]:
                return start
        return -1
```