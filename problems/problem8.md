# 8. String to Integer (atoi)

[Problem](https://leetcode.com/problems/string-to-integer-atoi/description/). Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.

COMMENT: 🤢

```python
class Solution:
    def myAtoi(self, s: str) -> int:
        inf = (-2)**31
        sup = 2**31 - 1
        nonchar = False
        digits = ''
        sign = 1

        for char in s:
            if not char.isdigit():
                if char == ' ':
                    if nonchar or digits: break
                    continue
                
                if digits: break

                if char == '-':
                    if nonchar: break
                    else: sign = -1; nonchar = True; continue

                if char == '+':
                    if nonchar: break
                    else: nonchar = True; continue

                break
            else:
                digits += char
        
        if not digits:
            return 0
        
        digits = sign * int(digits)
        
        if digits <= inf: return inf
        
        if digits >= sup: return sup
                
        return digits
```