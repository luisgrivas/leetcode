class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        size = len(needle)
        for start in range(len(haystack)):
            if needle in haystack[start:(start + size)]:
                return start
        return -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.strStr('aabcabc', 'abc'))