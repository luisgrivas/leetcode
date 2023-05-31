# 242. Valid Anagram

[Problem](). Given two strings s and t, return true if t is an anagram of s, and false otherwise.

There are several ways to solve this problem. One straightforward method is to compare the frequency of each character in the given strings. If the character counts differ, it indicates that the strings are not anagrams of each other.

```python3
def isAnagram4(self, s: str, t: str) -> bool:
	count1 = {}
    while s:
        ch = s[0]
        count1[ch] = s.count(ch)
        s = s.replace(ch, '')

    count2 = {}
    while t:
        ch = t[0]
        count2[ch] = t.count(ch)
        t = t.replace(ch, '')
    return count1 == count2
```
There is a more pythonic way to do this: ```count = {ch:s.count(ch) for ch in s}``. But apparently this is slower than the previous code. 

Another idea is to sort the strings and compare them. The code is very simple:

```python3
def isAnagram2(self, s: str, t: str) -> bool:
	return sorted(s) == sorted(t)
``
It is importatant to say that the complexity of this solution ($O(n log n + m log n)$) is worst than the first one ($O(m + n)$). 