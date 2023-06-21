class Solution:
    def myAtoi(self, s: str) -> int:
        inf = (-2)**31
        sup = 2**31 - 1
        nonchar = False
        digits = ''
        sign = 1

        for char in s:
            if not char.isdigit():
                if digits: break

                if char == ' ':
                    if nonchar or digits: break
                    continue

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
    


if __name__ == '__main__':
    solution = Solution()
    s = "000+1-42a1234"
    print(solution.myAtoi(s), 0)
    s = "  000213 asdas 22323   "
    print(solution.myAtoi(s), 213)
    s = "  asdjaklsdjklasd   "
    print(solution.myAtoi(s), 0)
    s = "     "
    print(solution.myAtoi(s), 0)
    s = ""
    print(solution.myAtoi(s), 0)
    s = "4193 with words"
    print(solution.myAtoi(s), 4193)
    s = "words and 987"
    print(solution.myAtoi(s), 0)
    s = "- 3 9."
    print(solution.myAtoi(s), 0)
    s = "+-12"
    print(solution.myAtoi(s), 0)
    s = "00000-42a1234"
    print(solution.myAtoi(s), 0)
    s = "      -+a12"
    print(solution.myAtoi(s), 0)
    s = "      +12"
    print(solution.myAtoi(s), 12)
    s = "+ +1 2"
    print(solution.myAtoi(s), 0)
    s = ".1"
    print(solution.myAtoi(s), 0)
    s = "w987"
    print(solution.myAtoi(s), 0)
    s = " 987"
    print(solution.myAtoi(s), 987)
    s = " -a987"
    print(solution.myAtoi(s), 0)
    s = "0  123"
    print(solution.myAtoi(s), 0)





