class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for ch in s:
            find = t.find(ch)
            if find >= 0:
                t = t[:find] + t[(find + 1):]
            else:
                return False
        return not t

    def isAnagram2(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    def isAnagram3(self, s: str, t: str) -> bool:
        count1 = {ch:s.count(ch) for ch in s}
        count2 = {ch:t.count(ch) for ch in t}
        return count1 == count2 

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

def isAnagram5(self, s: str, t: str) -> bool:
    u = s + t
    while u:
        ch = u[0]
        if s.count(u) != t.count(u):
            return False
        else:
            u = u.replace(ch, '')
    return True


if __name__ == '__main__':

    sol = Solution()
    tests = [['cacc', 'aacc'], ["anagram", "nagaram"],
    ["rat", "car"], ["a", "b"], ["ab", "a"], ["a", "ab"],
    ["bbb", "bb"], ["bb", "bb"] ]
    sols = [False, True, False, False, False, False, False, True]
    for i,v in enumerate(tests):
        print(v)
        assert sols[i] == sol.isAnagram5(v[0], v[1])
        