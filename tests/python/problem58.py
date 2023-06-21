class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
    
    def lengthOfLastWord2(self, s: str) -> int:
        s = s.rstrip()
        count = 0
        for el in s[::-1]:
            if el == ' ':
                break
            count += 1
        return count
    
    def lengthOfLastWord3(self, s: str) -> int:
        count = 0
        for el in s[::-1]:
            if el == ' ':
                if count > 0: break
            else: count += 1
        return count
    
    def lengthOfLastWord4(self, s: str) -> int:
        count = 0
        for ind in range(len(s) - 1, -1, -1):     
            if s[ind] == ' ':
                if count > 0: break
            else: count += 1
        return count






if __name__ == '__main__':
    import time
    solution = Solution()

    st = time.process_time()
    s = "   fly me   to   the moon           "
    print(solution.lengthOfLastWord(s), 4)

    s = "   fly me   to   the moon  "
    print(solution.lengthOfLastWord(s), 4)

    s = "luffy is still joyboy"
    print(solution.lengthOfLastWord(s), 6)

    s = "a a   a a aa a a a a "
    print(solution.lengthOfLastWord(s), 1)

    s = "        abbbb"
    print(solution.lengthOfLastWord(s), 5)

    s = "        a    aba      as     asd     asd   qqwe"
    print(solution.lengthOfLastWord(s), 4)

    et = time.process_time()
    print(et - st)


    st = time.process_time()
    s = "   fly me   to   the moon           "
    print(solution.lengthOfLastWord2(s), 4)

    s = "   fly me   to   the moon  "
    print(solution.lengthOfLastWord2(s), 4)

    s = "luffy is still joyboy"
    print(solution.lengthOfLastWord2(s), 6)

    s = "a a   a a aa a a a a "
    print(solution.lengthOfLastWord2(s), 1)

    s = "        abbbb"
    print(solution.lengthOfLastWord2(s), 5)

    s = "        a    aba      as     asd     asd   qqwe"
    print(solution.lengthOfLastWord2(s), 4)
    et = time.process_time()
    print(et - st)


    st = time.process_time()
    s = "   fly me   to   the moon           "
    print(solution.lengthOfLastWord3(s), 4)

    s = "   fly me   to   the moon  "
    print(solution.lengthOfLastWord3(s), 4)

    s = "luffy is still joyboy"
    print(solution.lengthOfLastWord3(s), 6)

    s = "a a   a a aa a a a a "
    print(solution.lengthOfLastWord3(s), 1)

    s = "        abbbb"
    print(solution.lengthOfLastWord3(s), 5)

    s = "        a    aba      as     asd     asd   qqwe"
    print(solution.lengthOfLastWord3(s), 4)
    et = time.process_time()
    print(et - st)


    st = time.process_time()
    s = "   fly me   to   the moon           "
    print(solution.lengthOfLastWord4(s), 4)

    s = "   fly me   to   the moon  "
    print(solution.lengthOfLastWord4(s), 4)

    s = "luffy is still joyboy"
    print(solution.lengthOfLastWord4(s), 6)

    s = "a a   a a aa a a a a "
    print(solution.lengthOfLastWord4(s), 1)

    s = "        abbbb"
    print(solution.lengthOfLastWord4(s), 5)

    s = "        a    aba      as     asd     asd   qqwe"
    print(solution.lengthOfLastWord4(s), 4)
    et = time.process_time()
    print(et - st)

