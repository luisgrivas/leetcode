"""
Given two binary strings a and b, return their sum as a binary string.
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        l = max(len(a), len(b))
        pairs = list(zip(a.zfill(l), b.zfill(l)))
        count = '0'
        output = '' 
        f = lambda x, y: '0' if x==y else '1'
        while pairs:
            ai, bi = pairs.pop()
            output = f(count, f(ai, bi)) + output
            if (ai != bi and count == '1') or (ai == bi == '1'):
                count = '1'
            else:
                count = '0'
        if count == '1':
            output = count + output
        return output
