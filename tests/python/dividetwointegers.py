"""
29. Divide Two Integers

Given two integers dividend and divisor, divide two integers without using multiplication, 
division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part.
For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within 
the 32-bit signed integer range: [−2^31, 2^31 − 1]. For this problem, if the quotient is 
strictly greater than 2^31 - 1, then return 2^31 - 1, and if the quotient is strictly less
than -2^31, then return -2^31.
"""

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign1 = 1 if dividend >= 0 else -1
        sign2 = 1 if divisor >= 0 else -1
        quotient = 1

        





if __name__ == '__main__':
    sol = Solution()
