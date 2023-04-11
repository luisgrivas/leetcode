# Palindrome Number

[Problem](https://leetcode.com/problems/palindrome-number/description/). Given an integer x, return true if x is a palindrome, and false otherwise.

To solve this problem, basically one has to find the "reversed" number and compare it with the given one.
There are several ways to do this. One way is to use simple arithmetic like the following.

```python3
class Solution:
    def isPalindrome(self, x: int) -> bool:
      rev = 0
      num = x
      while(num >= 1):
        rev = (rev * 10) + (num % 10)
        num = int(num / 10)
      return rev == x
```

I think this is the correct solution, but apparently this runs slowly. Using strings we can find a faster solution.

```python3
class Solution:
    def isPalindrome(self, x: int) -> bool:
      str_x = str(x)
      rev = str_x[::-1]
      return str_x == rev
```
I think that this solutions is like cheating but whatever.
